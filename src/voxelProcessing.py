import numpy as np
from scipy import sparse
from scipy import ndimage
import os
import time as t
import tempfile
'''
VoxelProcessing class implemented here which provide main() public method.
main() method create blocks of input numpy array and perform morphological operation on each block. after finishing the operation on it, will store output of each block in the file and then read data from that file and return whole array as output.
VoxelProcessing has input array as attribute along with that other attribute are, operation name and dictionary of parameters needed for that  operation plus number of blocks, extra border.
'''


class VoxelProcessing:

	def __init__(self,input_var,no_of_blocks,fakeghost,make_float32=True,operation="nothing",operationArgumentDic=""):
		'''
        Parameters
        ----------
        input_var            : type: 3D numpy array
        no_of_blocks         : type: int, number of frame(block) you want in input array with respect to x axis. ex = 4
        fakeghost            : type: int, extra border around block, generally with respect to structure element size. ex = 1
        make_float32         : type: boolean, do you want to type cast input numpy array to float32.
		operation            : type: string, morphological operation name, ex = binary_closing
		operationArgumentDic : type: dictionary, parameters for respective operation
		
		Returns
        -------
		Object of this class with all atribute.
        '''
		self.__X = input_var.shape[0]
		self.__Y = input_var.shape[1]
		self.__Z = input_var.shape[2]
		self.__make_float32 = make_float32
		print("Original input_var Size: ",input_var.nbytes/1000000000, "GB")
		if make_float32:
			self.__input_var = np.float32(input_var)
		else:
			self.__input_var = input_var
		self.__fakeghost = fakeghost	
		self.__sparsed = self.isSparse(input_var)
		self.__block_size, self.__no_of_blocks = self.get_block_size(input_var.shape[0],no_of_blocks)
		self.__operation = operation
		self.__operationArgumentDic = operationArgumentDic
		print("X: ",self.__X,"Y: ",self.__Y,"Z: ",self.__Z,"\nblock_size: ",self.__block_size,"\nfakeghost: ",self.__fakeghost,"\nsparsed: ",self.__sparsed,"\nno_of_blocks: ",self.__no_of_blocks,"\nmake_float32: ",make_float32,"\noperation: ",self.__operation)		
		
		
	# if more than 50% value are zero then matrix is sparse	
	def isSparse(self,input_var):
		'''
		check input array is sparse or not. Greater then 50% value are zero then consider as sparsed.
        Parameters
        ----------
        input_var            : type: 3D numpy array
        
		Returns
        -------
		boolean value : True if more then 50% value are zeros.
						False if more then 50% value are nonZeros.
        '''
		temp = np.count_nonzero(input_var)/input_var.size
		print("desity : ",temp)
		return (temp)<0.51	
		
	#based on x axis size and no_of_blocks return new number of block and block_size such that even partion happened. 		
	def get_block_size(self,axisSize,no_of_blocks):
		'''
		find blocksize based on given no of blocks such that block size become round value.
        Parameters
        ----------
        axisSize     : x axis value in input array.
		no_of_blocks : number of blocks you want
        
		Returns
        -------
		block_size    : type: int,each block size 
		no_of_blocks  : type: int,possible number of block such that it evenly divide array
        '''
		
		while(axisSize % no_of_blocks != 0 ):
			no_of_blocks -= 1
		
		return axisSize //no_of_blocks,no_of_blocks
	
	
	# this method will call by every morphological operation..		
	def main(self):
		'''
		Based on object parameter it perform our approach. create block then perform morphological operation and return processed array.    
        
		Returns
        -------
		outputArr : type: numpy array, Based on morphological operation you perform return, output array.
        '''
		file = tempfile.TemporaryFile(mode="wb")
		if self.__sparsed:			
			outputDtype = self.__sparsedOperation(file)		
		else:		
			outputDtype = self.__denseOperation(file)
		#file.close()		
		return self.__getDataFromBinaryFile(file,outputDtype=outputDtype)
		
	#if matrix sparse then this method will be called
	def __sparsedOperation(self,file):
		'''
		if input array is sparsed then it will first do compression and then create blocks and perform operation on each.   
        Parameters
        ----------
        file     : type: file object, in which you want to write binary output file of each block.
		Returns
        -------
		outputDtype : type: data type, of output array after morphological operation.
        '''
		print("sparsed Operation called................")	
		input_var = self.__getCompressed()
		total = input_var.data.nbytes + input_var.indptr.nbytes + input_var.indices.nbytes
		mem =  total / 1000000000
		print("compressed input_var Size: ", mem, "Gb")
		for i in range(self.__no_of_blocks):			
			jump,border = self.__getJumpAndBorder()
			block3d = self.__get3DblockFromCompressed(input_var,jump,border,blockNumber=i)						
			output = self.__operationTask(block3d)			
			ans = self.__removeBorder(output,i)			
			ans.tofile(file)		
			outputDtype = ans.dtype
		return outputDtype
			
	

	# if matrix is dense then this method will be called		
	def __denseOperation(self,file):
		'''
		if input array is dense then it will not do compression, directly create blocks and perform operation on each.   
        Parameters
        ----------
        file     : type: file object, in which you want to write binary output file of each block.
		Returns
        -------
		outputDtype : type: data type, of output array after morphological operation.
        '''
		print("dense Operation called................")		
		mem =  self.__input_var.nbytes / 1000000000
		print("Memory size after compression = ", mem, "Gb") #it will same as input_var if make_float32=false		
		for i in range(self.__no_of_blocks):	
			start_time = t.time()
			block3d = self.__get3dBlock(self.__input_var,blockNumber=i)			
			output = self.__operationTask(block3d)			
			ans = self.__removeBorder(output,i)			
			ans.tofile(file)			
			outputDtype = ans.dtype
		return outputDtype
			
			
	# input_var:3d array, output:csc compressed matrix	
	def __getCompressed(self):
		'''
		return CSC compressed array.   
        Parameters
        ----------
        Object input_var which will be 3D		
		Returns
        -------
		outputDtype : type: csc compressed matrix (2D) 
        '''	
		return sparse.csc_matrix(self.__input_var.reshape(self.__X*self.__Y,self.__Z))	
	
	# if your array is not compressed then call this method to get ith 3dblock.	
	def __get3dBlock(self,input_var,blockNumber):
		'''
		from 3d array return ith frame with respect to x axis with extra border.  
        Parameters
        ----------
        input_var  	: type: 3d input array
		blockNumber : type: int, ith block which you want with respect to x axis, or ith frame. ex= 5
		
		Returns
        -------
		3dblock     : type: array, ith frame, size: (1,y,z) with fakegost(extra border)
        '''
		startIndex = (self.__block_size*blockNumber)-self.__fakeghost
		endIndex = startIndex + self.__block_size + 2*self.__fakeghost
		if startIndex<0:
				startIndex =0	
		if endIndex > input_var.shape[0]:
			endIndex = input_var.shape[0]
		
		return input_var[startIndex:endIndex,:,:]
	
	#input_var: compressed array,block number, extra border output 3d array block.	
	def __get3DblockFromCompressed(self,input_var,jump,border,blockNumber):
		'''
		from comprassesd 2d array return ith frame with respect to x axis.  
        Parameters
        ----------
        input_var  	: type: 2d comprassed array
		jump        : type: int, blocksize in 2d compreesed array for 3d block.
		border      : type: int, calculated extra border value in 2d array for 3d block
		blockNumber : type: int, ith block which you want with respect to x axis, or ith frame. ex= 5
		
        Returns
		-------
		3dblock     : type: array, ith frame, size: (1,y,z) with fakegost(extra border)
        '''
		axisSize=self.__Y
		startIndex = blockNumber*jump - border
		endIndex = startIndex + jump + 2*border	
		if startIndex<0:
				startIndex =0	
		if endIndex > input_var.shape[0]:
			endIndex = input_var.shape[0]
		block_2d = input_var[startIndex:endIndex,:].toarray()		
		nz = block_2d.shape[0]/axisSize		
		return np.rollaxis(np.dstack(np.split(block_2d,nz)),-1)
		
	# border and jump calculation for compressed array to 3d ith block	
	def __getJumpAndBorder(self):
		'''
		form comprassesd 2d array find blocksize and fakeghost value for 3d block  
        Parameters
        ----------
        input_var  	: type: 2d comprassed array	
		
        Returns
		-------
		jump        : type: int, blocksize in 2d compreesed array for 3d block.
		border      : type: int, calculated extra border value in 2d array for 3d block
        '''
		axisSize=self.__Y
		return axisSize*self.__block_size,axisSize*self.__fakeghost

	

	def __removeBorder(self,input_var,blockNumber):
		'''
		form 3d block remove extra border(fakeghost cells).  
        Parameters
        ----------
        input_var  	: type: 3d numpy array, output array (ith block) after mprpological operation
		blockNumber : type: int, ith block.
		
        Returns
		-------
		3dblock     : type: array, block without extra border(fakeghost cells).
        '''
		if blockNumber == 0:
			ans = input_var[:self.__block_size,:,:]
		elif blockNumber == (self.__no_of_blocks - 1):
			ans = input_var[self.__fakeghost:,:,:]
		else:
			ans = input_var[self.__fakeghost:self.__block_size+self.__fakeghost,:,:]		
		return ans
				
	def __getDataFromBinaryFile(self,file,outputDtype):
		'''
		create output numpy array from stored binarry file. 
        Parameters
        ----------
        file  	: type: file object, file in which you store each block output.
		outputDtype : type: data type, morphological operation output data type.
		
        Returns
		-------
		finaloutput     : type: 3d array, output of operation whole array.
        '''
				
		shape=(self.__X,self.__Y,self.__Z)
		tempfile = np.memmap(file,shape=shape,dtype = outputDtype)			
		file.close()			
		return tempfile
		
	
	# D = operationArgumentDic  paraeters required for specific operations.		
	def __operationTask(self,input_var):
		'''
		perform respective moephological operation on input block.
        Parameters
        ----------
        input_var  	: type: 3d numpy array, ith block.		
		
        Returns
		-------
		output     : type: 3d array, output of operation, ith block array.
        '''
		
		#can't do binary_fill_holes operation because it is not local...need whole image information. 
		D=self.__operationArgumentDic
		if self.__operation=="binary_closing":	
			return ndimage.binary_closing(input_var, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
		elif self.__operation=="binary_dilation":
			return ndimage.binary_dilation(input_var, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
		elif self.__operation=="binary_erosion":
			return ndimage.binary_erosion(input_var, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
		elif self.__operation=="binary_fill_holes":
			return ndimage.binary_fill_holes(input_var, structure=D["structure"],output=D["output"], origin=D["origin"])
		elif self.__operation=="binary_hit_or_miss":
			return ndimage.binary_hit_or_miss(input_var, structure1=D["structure1"],structure2=D["structure2"],output=D["output"], origin1=D["origin1"], origin2=D["origin2"])
		elif self.__operation=="binary_opening":
			return ndimage.binary_opening(input_var, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
		elif self.__operation=="binary_propagation":			
			return ndimage.binary_propagation(input_var, structure=D["structure"],output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"])
		elif self.__operation=="black_tophat":
			return ndimage.black_tophat(input_var, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="grey_dilation":
			return ndimage.grey_dilation(input_var, structure=D["structure"],size=D["size"], footprint=D["footprint"],output=D["output"], mode=D["mode"], cval=D["cval"], origin=D["origin"])			
		elif self.__operation=="grey_closing":
			return ndimage.grey_closing(input_var, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="grey_erosion":
			return ndimage.grey_erosion(input_var, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="grey_opening":
			return ndimage.grey_opening(input_var, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="morphological_gradient":
			return ndimage.morphological_gradient(input_var, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="morphological_laplace":
			return ndimage.morphological_laplace(input_var, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="white_tophat":
			return ndimage.white_tophat(input_var, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="multiply":
			return input_var*D["scalar"]		
		else:
			return input_var # no operation performed....
			
	
		
		
	

	
		
		

	
	
	
	
	
	

	
	
	



	

	
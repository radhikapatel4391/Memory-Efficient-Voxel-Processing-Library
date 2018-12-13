import numpy as np
from scipy import sparse
from scipy import ndimage
import os
import multiprocessing
#from memory import Memory
#from tempfile import TemporaryFile

class VoxelProcessing:

	def __init__(self,input,blockSize,fakeGhost,makeFloat32=True,operation="nothing",operationArgumentDic=""):
		self.__X = input.shape[0]
		self.__Y = input.shape[1]
		self.__Z = input.shape[2]
		self.__makeFloat32 = makeFloat32
		print("Original input Size: ",input.nbytes/1000000000, "GB")
		if makeFloat32:
			self.__input = np.float32(input)
		else:
			self.__input = input
		self.__fakeGhost = fakeGhost	
		self.__sparsed = self.isSparse(input)
		self.__nBlocks,self.__blockSize = self.getNumberOfBlock(input.shape[0],blockSize)
		self.__operation = operation
		self.__operationArgumentDic = operationArgumentDic
		print("X: ",self.__X,"Y: ",self.__Y,"Z: ",self.__Z,"blockSize: ",self.__blockSize,"fakeGhost: ",self.__fakeGhost,"sparsed: ",self.__sparsed,"nBlocks: ",self.__nBlocks)		
		#self.M = Memory()
		#self.M.add_mem()#.....................................................................................................
		
	# if more than 50% value are zero then matrix is sparse	
	def isSparse(self,input):
		return (np.count_nonzero(input)/input.size)<0.51	
		
	#based on axis size and block size return number of block and new blockSize such that even partion happened. 		
	def getNumberOfBlock(self,axisSize,blockSize):		
		while(axisSize % blockSize!=0):
			blockSize -= 1
		
		return axisSize //blockSize,blockSize
	
	
	# this method will call by every operation..		
	def main(self):		
		file = open(self.__operation, "wb")
		if self.__sparsed:			
			outputDtype = self.__sparsedOperation(file)		
		else:		
			outputDtype = self.__denseOperation(file)
		file.close()
		#self.M.add_mem()#.....................................................................................................	
		return self.__getDataFromBinaryFile(filename=self.__operation,outputDtype=outputDtype)
		
	#if matrix sparse then block operation happen
	def __sparsedOperation(self,file):
		print(".............sparsed method called............")
		input = self.__getCompressed()
		total = input.data.nbytes + input.indptr.nbytes + input.indices.nbytes
		mem =  total / 1000000000
		print("Memory size after compression = ", mem, "Gb")
		outputans = []
		jobs = []
		def spawn(j,outputans):
			jump,border = self.__getJumpAndBorder()
			block3d = self.__get3DblockFromCompressed(input,jump,border,blockNumber=j)
			output = self.__operationTask(block3d)
			outputans[j] = self.__removeBorder(output,j)
		for i in range(self.__nBlocks):
			p = multiprocessing.Process(target = spawn, args=(i,outputans))
			jobs.append(p)
			p.start()
		for proc in jobs:
			proc.join()
		for ans in outputans:
			ans.tofile(file)
		
		return outputans[0].dtype
			#self.M.add_mem()#.....................................................................................................
	

	# if matrix is dense and compression not happen then block operation		
	def __denseOperation(self,file):
		print(".............dense method called................")		
		mem =  self.__input.nbytes / 1000000000
		print("Memory size after compression = ", mem, "Gb") #it will same as input if makeFloat32=false
		for i in range(self.__nBlocks):			
			block3d = self.__get3dBlock(self.__input,blockNumber=i)
			output = self.__operationTask(block3d)
			ans = self.__removeBorder(output,i)
			ans.tofile(file)
			outputDtype = ans.dtype
		return outputDtype
			#self.M.add_mem()#.....................................................................................................
			
	# input:3d array output:csc compressed matrix, if matrix is sparse otherwise none	
	def __getCompressed(self):	
		return sparse.csc_matrix(self.__input.reshape(self.__X*self.__Y,self.__Z))	
	
	# if you array is not compressed then call this method for subblock	
	def __get3dBlock(self,input,blockNumber):
		startIndex = (self.__blockSize*blockNumber)-self.__fakeGhost
		endIndex = startIndex + self.__blockSize + 2*self.__fakeGhost
		if startIndex<0:
				startIndex =0	
		if endIndex > input.shape[0]:
			endIndex = input.shape[0]
		#self.M.add_mem()#.....................................................................................................	
		return input[startIndex:endIndex,:,:]
	
	#input: compressed array,block number, extra border output 3d array block.	
	def __get3DblockFromCompressed(self,input,jump,border,blockNumber):	
		axisSize=self.__Y
		startIndex = blockNumber*jump - border
		endIndex = startIndex + jump + 2*border	
		if startIndex<0:
				startIndex =0	
		if endIndex > input.shape[0]:
			endIndex = input.shape[0]
		block_2d = input[startIndex:endIndex,:].toarray()		
		nz = block_2d.shape[0]/axisSize		
		#self.M.add_mem()#.....................................................................................................
		return np.rollaxis(np.dstack(np.split(block_2d,nz)),-1)
		
	# border and jump calculation for compressed array to 3d sub block	
	def __getJumpAndBorder(self):
		axisSize=self.__Y
		return axisSize*self.__blockSize,axisSize*self.__fakeGhost

	

	def __removeBorder(self,input,blockNumber):
		#self.M.add_mem()#.....................................................................................................
		if blockNumber == 0:
			ans = input[:self.__blockSize,:,:]
		elif blockNumber == (self.__nBlocks - 1):
			ans = input[self.__fakeGhost:,:,:]
		else:
			ans = input[self.__fakeGhost:self.__blockSize+self.__fakeGhost,:,:]		
		return ans
				
	def __getDataFromBinaryFile(self,filename,outputDtype):
		shape=(self.__X,self.__Y,self.__Z)
		try:
			file = open(filename, 'r')		
		except:
			print('Cannot open', filename)
			return 0
		else:
			tempfile = np.memmap(filename,shape=shape,dtype = outputDtype)			
			file.close()									
			return tempfile
	
	# D = operationArgumentDic  arguments required for specific operations.		
	def __operationTask(self,input):
		D=self.__operationArgumentDic
		#self.M.add_mem()#.....................................................................................................
		
		if self.__operation=="binary_closing":	
			return ndimage.binary_closing(input, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
		elif self.__operation=="binary_dilation":
			return ndimage.binary_dilation(input, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
		elif self.__operation=="binary_erosion":
			return ndimage.binary_erosion(input, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
		elif self.__operation=="binary_fill_holes":
			return ndimage.binary_fill_holes(input, structure=D["structure"],output=D["output"], origin=D["origin"])
		elif self.__operation=="binary_hit_or_miss":
			return ndimage.binary_hit_or_miss(input, structure1=D["structure1"],structure2=D["structure2"],output=D["output"], origin1=D["origin1"], origin2=D["origin2"])
		elif self.__operation=="binary_opening":
			return ndimage.binary_opening(input, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
		elif self.__operation=="binary_propagation":			
			return ndimage.binary_propagation(input, structure=D["structure"],output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"])
		elif self.__operation=="black_tophat":
			return ndimage.black_tophat(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="grey_dilation":
			return ndimage.grey_dilation(input, structure=D["structure"],size=D["size"], footprint=D["footprint"],output=D["output"], mode=D["mode"], cval=D["cval"], origin=D["origin"])
		elif self.__operation=="grey_closing":
			return ndimage.grey_closing(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="grey_erosion":
			return ndimage.grey_erosion(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="grey_opening":
			return ndimage.grey_opening(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="morphological_gradient":
			return ndimage.morphological_gradient(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="morphological_laplace":
			return ndimage.morphological_laplace(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="white_tophat":
			return ndimage.white_tophat(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
		elif self.__operation=="intMultiply":
			return input*D["scalar"]
		
		else:
			return input
			
	
		
		
	

	
		
		

	
	
	
	
	
	

	
	
	



	

	
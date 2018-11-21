import numpy as np
from scipy import sparse
from scipy import ndimage
import os


class VoxelProcessing:

	def __init__(self,input,blockSize,fakeGhost,operation="nothing",operationArgumentDic=""):
		self.__X = input.shape[0]
		self.__Y = input.shape[1]
		self.__Z = input.shape[2]
		self.__input = input		
		self.__fakeGhost = fakeGhost	
		self.__sparsed = self.isSparse(input)
		self.__nBlocks,self.__blockSize = self.getNumberOfBlock(input.shape[0],blockSize)
		self.__operation = operation
		self.__operationArgumentDic = operationArgumentDic
		print("X: ",self.__X,"Y: ",self.__Y,"Z: ",self.__Z,"blockSize: ",self.__blockSize,"fakeGhost: ",self.__fakeGhost,"sparsed: ",self.__sparsed,"nBlocks: ",self.__nBlocks)
		
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
			self.__sparsedOperation(file)		
		else:		
			self.__denseOperation(file)
		file.close()	
		return self.__getDataFromBinaryFile(filename=self.__operation)
		
	#if matrix sparse then block operation happen
	def __sparsedOperation(self,file):
		print(".............sparsedmethod called")
		input = self.__getCompressed()
		for i in range(self.__nBlocks):
			jump,border = self.__getJumpAndBorder()
			block3d = self.__get3DblockFromCompressed(input,jump,border,blockNumber=i)
			output = self.__operationTask(block3d)
			self.__removeBorder(output,i).tofile(file)
	

	# if matrix is dense and compression not happen then block operation		
	def __denseOperation(self,file):
		print(".............dense called................")
		for i in range(self.__nBlocks):			
			block3d = self.__get3dBlock(self.__input,blockNumber=i)
			output = self.__operationTask(block3d)
			self.__removeBorder(output,i).tofile(file)
			
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
		#return np.dstack(np.split(block_2d,nz))
		return np.rollaxis(np.dstack(np.split(block_2d,nz)),-1)
		
	# border and jump calculation for compressed array to 3d sub block	
	def __getJumpAndBorder(self):
		axisSize=self.__Y
		return axisSize*self.__blockSize,axisSize*self.__fakeGhost

	# D = operationArgumentDic  arguments required for specific operations.		
	def __operationTask(self,input):
		D=self.__operationArgumentDic
		if self.__operation=="dilation":
			return ndimage.grey_dilation(input, structure=D["structure"],size=D["size"], footprint=D["footprint"],output=D["output"], mode=D["mode"], cval=D["cval"], origin=D["origin"])
		elif self.__operation=="closing":
			return ndimage.binary_closing(input, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
		else:
			return input

	def __removeBorder(self,input,blockNumber):
		if blockNumber == 0:
			return input[:self.__blockSize,:,:]
		elif blockNumber == (self.__nBlocks - 1):
			return input[self.__fakeGhost:,:,:]
		else:
			return input[self.__fakeGhost:self.__blockSize+self.__fakeGhost,:,:]
				
	def __getDataFromBinaryFile(self,filename):
		shape=(self.__X,self.__Y,self.__Z)
		try:
			file = open(filename, 'r')		
		except:
			print('Cannot open', filename)
			return 0
		else:
			#merging = np.memmap(filename,shape=shape,dtype=np.float64)		
			np.save("output.npy", np.memmap(filename,shape=shape,dtype=np.float64))
			file.close()
			return np.load("output.npy")
		
	
	
		
		
	

	
		
		

	
	
	
	
	
	

	
	
	



	

	
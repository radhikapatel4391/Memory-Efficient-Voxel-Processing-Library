import numpy as np
from scipy import sparse
from scipy import ndimage
import os

#Global variables for file....which will reset by setGlobalValue function based on image..
X,Y,Z = 200,200,200
SPARSED = True
BLOCKSIZE = 20
NBLOCKS = 10
FG = 1


def getDataFromBinaryFile(filename,shape=(X,Y,Z)):
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
		
def removeBorder(input,blockNumber,nBlocks=NBLOCKS,blockSize=BLOCKSIZE):
	if blockNumber == 0:
		return input[:blockSize,:,:]
	elif blockNumber== nBlocks-1:
		return input[1:,:,:]
	else:
		return input[1:blockSize+1,:,:]
		
# D = operationArgumentDic  arguments required for specific operations.		
def operationTask(input,operation,D):
	if operation=="dilation":
		return ndimage.grey_dilation(input, structure=D["structure"],size=D["size"], footprint=D["footprint"],output=D["output"], mode=D["mode"], cval=D["cval"], origin=D["origin"])
	elif operation=="closing":
		return ndimage.binary_closing(input, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
	else:
		return input
		
		
# if you array is not compressed then call this method for subblock	
def get3dBlock(input,blockNumber,nBlocks=NBLOCKS,blockSize=BLOCKSIZE,fakeGhost=FG):
	startIndex = blockSize*blockNumber-1
	endIndex = startIndex + blockSize + 2
	if startIndex<0:
			startIndex =0	
	if endIndex > input.shape[0]:
		endIndex = input.shape[0]
		
	return input[startIndex:endIndex,:,:]
	
#input: compressed array,block number, extra border output 3d array block.	
def get3DblockFromCompressed(input,jump,border,blockNumber,axisSize=Y):	 
	startIndex = blockNumber*jump - border
	endIndex = startIndex + jump + 2*border	
	if startIndex<0:
			startIndex =0	
	if endIndex > input.shape[0]:
		endIndex = input.shape[0]
	block_2d = input[startIndex:endIndex,:].toarray()
	nz = (endIndex-startIndex)/axisSize	
	return np.rollaxis(np.dstack(np.split(block_2d,nz)),-1)

# border and jump calculation for compressed array to 3d sub block	
def getJumpAndBorder(fakeGhost=FG,axisSize=Y,blockSize=BLOCKSIZE):
	return axisSize*blockSize,axisSize*fakeGhost
		
# input:3d array output:csc compressed matrix, if matrix is sparse otherwise none	
def getCompressed(input):	
	return sparse.csc_matrix(input.reshape(X*Y,Z))	

	
#if matrix sparse then block operation happen
def sparsedOperation(input,operation,file,operationArgumentDic):
	print(".............sparsedmethod called")
	input = getCompressed(input)
	for i in range(NBLOCKS):
		jump,border = getJumpAndBorder()
		block3d = get3DblockFromCompressed(input,jump,border,blockNumber=i)
		output = operationTask(block3d,operation,operationArgumentDic)
		removeBorder(output,i).tofile(file)
	

# if matrix is dense and compression not happen then block operation		
def denseOperation(input,operation,file,operationArgumentDic):
	print(".............dense called................")
	for i in range(NBLOCKS):			
		block3d = get3dBlock(input,blockNumber=i)
		output = operationTask(block3d,operation,operationArgumentDic)
		removeBorder(output,i).tofile(file)
	
	
#based on axis size and block size return number of block and new blockSize such that even partion happened. 		
def getNumberOfBlock(blockSize=BLOCKSIZE,axisSize=X):
	while(axisSize % blockSize!=0):
		blockSize -= 1
	BLOCKSIZE = blockSize
	return axisSize // blockSize , blockSize
	
# if more than 50% value are zero then matrix is sparse	
def isSparse(input):
	return (np.count_nonzero(input)/input.size)<0.51
	
	
#will set Global variables with respect to file..	
def setGlobalValue(input,blockSize,fakeGhost):
	X = input.shape[0]
	Y = input.shape[1]
	Z = input.shape[2]
	BLOCKSIZE = blockSize
	FG = fakeGhost	
	SPARSED = isSparse(input)
	NBLOCKS = getNumberOfBlock()
	print(X,Y,Z,BLOCKSIZE,FG,SPARSED,NBLOCKS)
	return SPARSED
	
	
# this method will call by every operation..		
def main(input,blockSize,fakeGhost,operation="nothing",operationArgumentDic=""):
	
	s = setGlobalValue(input,blockSize,fakeGhost)
	file = open(operation, "wb")
	if s:
		print(s)
		sparsedOperation(input,operation,file,operationArgumentDic)		
	else:		
		denseOperation(input,operation,file,operationArgumentDic)
	file.close()	
	return getDataFromBinaryFile(filename=operation)


	

	
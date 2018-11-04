import numpy as np
import os
import sys
from scipy import sparse
from scipy import ndimage
import gc
X,Y,Z = 200,200,200
SPARSED = True
BLOCKSIZE = 20
NBLOCKS = 10
FG = 1
def grey_dilation(input,blockSize=20,fakeGhost=1, size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	x = input.shape[0]
	y = input.shape[1]
	z = input.shape[2]
	input = input.reshape(x*y,z)
	print("size before compresion: ",input.nbytes)
	while(x % blockSize!=0):
		blockSize -= 1
	n_blocks = x // blockSize
	input = sparse.csc_matrix(input)        
	sparse.save_npz("CRS.npz", input)
	startIndex = 0
	fake_ghost = 1
	jump = y*blockSize
	border = y*fake_ghost
	endIndex = jump + border
	if endIndex > input.shape[0]:
		endIndex = input.shape[0]
	f_handle = open('binary1', 'wb')
	for i in range(n_blocks):
		print("Start Index = ",startIndex)
		print("End Index = ", endIndex)
		block_2d = input[startIndex:endIndex,:].toarray()
		print("2d image shape: ",block_2d.shape)
		#block_2d = block_2d.T
		print("2d image shape after T: ",block_2d.shape)
		nz = (endIndex-startIndex)/y
		print("split for 3d: ",nz,block_2d.shape)
		mylist = np.split(block_2d,nz)
		block_3d = np.dstack(mylist)
		block_3d = np.rollaxis(block_3d,-1)
		print("after magic: ",block_3d.shape)
		#dilated = ndimage.grey_dilation(block_3d, structure=structure)
		dilated = block_3d
		print("dilated image shape: ",dilated.shape)
		if i == 0:
			dilated = dilated[:blockSize,:,:]
		elif i == n_blocks - 1:
			dilated = dilated[1:,:,:]
		else:
			dilated = dilated[1:blockSize+1,:,:]
		#.....
		print("dilated shape which I am writing: ",dilated.shape)
		dilated.tofile(f_handle)
		startIndex = endIndex - 2*border
		if startIndex<0:
			startIndex =0
		endIndex  += jump
		if endIndex > input.shape[0]:
			endIndex = input.shape[0]
		gc.collect()
	f_handle.close()
	try:
		merging = open("binary1", 'r')
		print("binary file object size: ",sys.getsizeof(merging))
	except:
		print('Cannot open', "binary1")
		return 0
	else:
		merging = np.memmap("binary1",shape=(x,y,z),dtype=np.float64)
		print("My shape: ",merging.shape,merging.dtype)
		np.save("output.npy", merging)
		return merging
		


	


		
	




	

	

	
def getDataFromBinaryFile(filename="binary",shape=(X,Y,Z)):
	try:
		merging = open(filename, 'r')		
	except:
		print('Cannot open', filename)
		return 0
	else:
		return np.memmap(filename,shape=shape,dtype=np.float64)
		
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
	
def getJumpAndBorder(fakeGhost=FG,axisSize=Y,blockSize=BLOCKSIZE):
	return axisSize*blockSize,axisSize*fakeGhost
		
# input:3d array output:csc compressed matrix, if matrix is sparse otherwise none	
def getCompressed(input):	
	return sparse.csc_matrix(input.reshape(X*Y,Z))	

	
#if matrix sparse then block operation happen
def sparsedOperation(input,operation,file,operationArgumentDic):
	input = getCompressed(input)
	for i in range(NBLOCKS):
		jump,border = getJumpAndBorder()
		block3d = get3DblockFromCompressed(input,jump,border,blockNumber=i)
		output = operationTask(block3d,operation,operationArgumentDic)
		removeBorder(output,i).tofile(file)

# if matrix is dense and compression not happen then block operation		
def denseOperation(input,operation,file,operationArgumentDic):
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
	return (np.count_nonzero(input)/input.size)<0.5
	
def setGlobalValue(input,blockSize,fakeGhost):
	X = input.shape[0]
	Y = input.shape[1]
	Z = input.shape[2]
	BLOCKSIZE = blockSize
	FG = fakeGhost	
	SPARSED = isSparse(input)
	NBLOCKS = getNumberOfBlock()
	print(X,Y,Z,BLOCKSIZE,FG,SPARSED,NBLOCKS)
		
def main(input,blockSize,fakeGhost,operation="",operationArgumentDic=""):
	
	setGlobalValue(input,blockSize,fakeGhost)
	file = open('binary', 'wb')
	if SPARSED:
		sparsedOperation(input,operation,file,operationArgumentDic)		
	else:		
		denseOperation(input,operation,file,operationArgumentDic)
	file.close()
	return getDataFromBinaryFile()

	
def nothing(input,blockSize=20,fakeGhost=1,):
	return main(input,blockSize,fakeGhost)
	
filename = 'gyroidUniform.npy'   
structure = np.ones((3,3,3))
input = np.load(filename, mmap_mode="r")
output = nothing(input)
print((input==output).all())
l = np.load("output.npy")
print(l.dtype,input.dtype,(input==l).all())	
	
	
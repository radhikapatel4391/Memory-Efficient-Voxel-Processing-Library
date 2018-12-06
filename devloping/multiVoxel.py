import numpy as np
from scipy import sparse
from scipy import ndimage
import os
import multiprocessing

def isSparse(input):
	return (np.count_nonzero(input)/input.size)<0.51	
	
#based on axis size and block size return number of block and new blockSize such that even partion happened. 		
def getNumberOfBlock(axisSize,blockSize):		
	while(axisSize % blockSize!=0):
		blockSize -= 1
	
	return axisSize //blockSize,blockSize
	
	
	
#................................................parameter setting......
structure = np.ones((3,3,3))	
filename = 'gyroidUniform.npy'   		
input = np.load(filename, mmap_mode="r")
X = input.shape[0]
Y = input.shape[1]
Z = input.shape[2]
makeFloat32 = False
print("Original input Size: ",input.nbytes/1000000000, "GB")
if makeFloat32:
	input = np.float32(input)
else:
	input = input
fakeGhost = 4	
sparsed = isSparse(input)
nBlocks,blockSize = getNumberOfBlock(input.shape[0],50)
operation = "nothing"
operationArgumentDic = {}
print("X: ",X,"Y: ",Y,"Z: ",Z,"blockSize: ",blockSize,"fakeGhost: ",fakeGhost,"sparsed: ",sparsed,"nBlocks: ",nBlocks)	

#........................................

# this method will call by every operation..		
def main():		
	file = open(operation, "wb")
	if sparsed:			
		outputDtype = sparsedOperation(file)		
	else:		
		outputDtype = denseOperation(file)
	file.close()
	#self.M.add_mem()#.....................................................................................................	
	return getDataFromBinaryFile(filename=operation,outputDtype=outputDtype)
	
#if matrix sparse then block operation happen
def sparsedOperation(file):
	print(".............sparsed method called............")
	input = getCompressed()
	total = input.data.nbytes + input.indptr.nbytes + input.indices.nbytes
	mem =  total / 1000000000
	print("Memory size after compression = ", mem, "Gb")
	for i in range(nBlocks):
		jump,border = getJumpAndBorder()
		block3d = get3DblockFromCompressed(input,jump,border,blockNumber=i)
		output = operationTask(block3d)
		ans = removeBorder(output,i)
		ans.tofile(file)
		outputDtype = ans.dtype
	return outputDtype
		#self.M.add_mem()#.....................................................................................................

def action(i,file):
		block3d = get3dBlock(input,blockNumber=i)
		output = operationTask(block3d)
		ans = removeBorder(output,i)
		ans.tofile(file)
		#outputDtype = ans.dtype
# if matrix is dense and compression not happen then block operation		
def denseOperation(file):
	print(".............dense method called................")		
	mem =  input.nbytes / 1000000000
	print("Memory size after compression = ", mem, "Gb") #it will same as input if makeFloat32=false	
	for i in range(nBlocks):			
		p = multiprocessing.Process(target=action, args=(i,file))        
		p.start()
	return "float64"
		#self.M.add_mem()#.....................................................................................................
		
# input:3d array output:csc compressed matrix, if matrix is sparse otherwise none	
def getCompressed():	
	return sparse.csc_matrix(input.reshape(X*Y,Z))	

# if you array is not compressed then call this method for subblock	
def get3dBlock(input,blockNumber):
	startIndex = (blockSize*blockNumber)-fakeGhost
	endIndex = startIndex + blockSize + 2*fakeGhost
	if startIndex<0:
			startIndex =0	
	if endIndex > input.shape[0]:
		endIndex = input.shape[0]
	#self.M.add_mem()#.....................................................................................................	
	return input[startIndex:endIndex,:,:]

#input: compressed array,block number, extra border output 3d array block.	
def get3DblockFromCompressed(input,jump,border,blockNumber):	
	axisSize=Y
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
def getJumpAndBorder():
	axisSize=Y
	return axisSize*blockSize,axisSize*fakeGhost



def removeBorder(input,blockNumber):
	#self.M.add_mem()#.....................................................................................................
	if blockNumber == 0:
		ans = input[:blockSize,:,:]
	elif blockNumber == (nBlocks - 1):
		ans = input[fakeGhost:,:,:]
	else:
		ans = input[fakeGhost:blockSize+fakeGhost,:,:]		
	return ans
			
def getDataFromBinaryFile(filename,outputDtype):
	shape=(X,Y,Z)
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
def operationTask(input):
	D=operationArgumentDic
	#self.M.add_mem()#.....................................................................................................
	
	if operation=="binary_closing":	
		return ndimage.binary_closing(input, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
	elif operation=="binary_dilation":
		return ndimage.binary_dilation(input, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
	elif operation=="binary_erosion":
		return ndimage.binary_erosion(input, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
	elif operation=="binary_fill_holes":
		return ndimage.binary_fill_holes(input, structure=D["structure"],output=D["output"], origin=D["origin"])
	elif operation=="binary_hit_or_miss":
		return ndimage.binary_hit_or_miss(input, structure1=D["structure1"],structure2=D["structure2"],output=D["output"], origin1=D["origin1"], origin2=D["origin2"])
	elif operation=="binary_opening":
		return ndimage.binary_opening(input, structure=D["structure"], iterations=D["iterations"], output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"], brute_force=D["brute_force"])
	elif operation=="binary_propagation":			
		return ndimage.binary_propagation(input, structure=D["structure"],output=D["output"], origin=D["origin"], mask=D["mask"], border_value=D["border_value"])
	elif operation=="black_tophat":
		return ndimage.black_tophat(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
	elif operation=="grey_dilation":
		return ndimage.grey_dilation(input, structure=D["structure"],size=D["size"], footprint=D["footprint"],output=D["output"], mode=D["mode"], cval=D["cval"], origin=D["origin"])
	elif operation=="grey_closing":
		return ndimage.grey_closing(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
	elif operation=="grey_erosion":
		return ndimage.grey_erosion(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
	elif operation=="grey_opening":
		return ndimage.grey_opening(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
	elif operation=="morphological_gradient":
		return ndimage.morphological_gradient(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
	elif operation=="morphological_laplace":
		return ndimage.morphological_laplace(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
	elif operation=="white_tophat":
		return ndimage.white_tophat(input, structure=D["structure"], size=D["size"], footprint=D["footprint"],  output=D["output"], origin=D["origin"],mode=D["mode"], cval=D["cval"])
	elif operation=="intMultiply":
		return input*D["scalar"]
	
	else:
		return input
		
if __name__ == '__main__':
	print("\n nothing testing...")
	output = main()
	print("\nresult: ",(input==output).all())
	print(output.dtype,input.dtype)
	
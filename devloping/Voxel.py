from voxelProcessing import VoxelProcessing
import numpy as np

#Doing not any operation ...	
def nothing(input,blockSize=50,fakeGhost=1,makeFloat32=True):
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32)
	return v.main()
	# M.add_mem()#.....................................................................................................
	# M.print_memory_usage()
	# print(M.getmemoryList())
	# return I
	
#function...
# def grey_dilation(input,blockSize=50,fakeGhost<=1,makeFloat32=True,size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	# if fakeGhost<=1:
		# fakeGhost = structure.shape[0]//2
	# operationArgumentDic = {"size":size,"footprint":footprint,"structure":structure,"output":output,"mode":mode,"cval":cval,"origin":origin}	
	# v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="grey_dilation",operationArgumentDic=operationArgumentDic)
	# I,M = v.main()
	# M.add_mem()#.....................................................................................................
	# M.print_memory_usage()
	# print(M.getmemoryList())
	# return I
	


def binary_dilation(input,blockSize=50,fakeGhost=1,makeFloat32=True, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False):

	if fakeGhost<=1:
		if structure is not None:
			fakeGhost = structure.shape[0]//2
		
	operationArgumentDic = {"structure":structure,"iterations":iterations,"output":output,"origin":origin,"mask":mask, "border_value":border_value, "brute_force":brute_force}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="binary_dilation",operationArgumentDic=operationArgumentDic)
	return v.main()	
	
def binary_erosion(input,blockSize=50,fakeGhost=1,makeFloat32=True, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False):

	if fakeGhost<=1:
		if structure is not None:
			fakeGhost = structure.shape[0]//2
		
	operationArgumentDic = {"structure":structure,"iterations":iterations,"output":output,"origin":origin,"mask":mask, "border_value":border_value, "brute_force":brute_force}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="binary_erosion",operationArgumentDic=operationArgumentDic)
	return v.main()		

def binary_closing(input,blockSize=50,fakeGhost=2,makeFloat32=True, structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False):

	if fakeGhost<=2:
		if structure is not None:
			t = structure.shape[0]//2
			if t > fakeGhost:
				fakeGhost = t
		
	operationArgumentDic = {"structure":structure,"iterations":iterations,"output":output,"origin":origin,"mask":mask, "border_value":border_value, "brute_force":brute_force}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="binary_closing",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def binary_opening(input,blockSize=50,fakeGhost=2,makeFloat32=True,  structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False):

	if fakeGhost<=2:
		if structure is not None:
			t = structure.shape[0]//2
			if t > fakeGhost:
				fakeGhost = t
		
	operationArgumentDic = {"structure":structure,"iterations":iterations,"output":output,"origin":origin,"mask":mask, "border_value":border_value, "brute_force":brute_force}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="binary_opening",operationArgumentDic=operationArgumentDic)
	return v.main()	
	

	
def binary_fill_holes(input,blockSize=50,fakeGhost=1,makeFloat32=True, structure=None, output=None, origin=0):

	if fakeGhost<=1:
		if structure is not None:
			fakeGhost = structure.shape[0]//2
		
	operationArgumentDic = {"structure":structure,"output":output,"origin":origin}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="binary_fill_holes",operationArgumentDic=operationArgumentDic)
	return v.main()	
	
def binary_hit_or_miss(input, blockSize=50,fakeGhost=1,makeFloat32=True, structure1=None, structure2=None, output=None, origin1=0, origin2=None):

	if fakeGhost<=1:
		if structure1 is not None:
			fakeGhost = structure1.shape[0]//2
		
	operationArgumentDic = {"structure1":structure1,"structure2":structure2,"output":output,"origin1":origin1,"origin2":origin2}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="binary_hit_or_miss",operationArgumentDic=operationArgumentDic)
	return v.main()
	

def binary_propagation(input,blockSize=50,fakeGhost=1,makeFloat32=True, structure=None, mask=None, output=None, border_value=0, origin=0):
	if fakeGhost<=1:
		if structure is not None:
			fakeGhost = structure.shape[0]//2
		
	operationArgumentDic = {"structure":structure,"output":output,"origin":origin,"mask":mask, "border_value":border_value}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="binary_propagation",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def black_tophat(input,blockSize=50,fakeGhost=2,makeFloat32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):

	if fakeGhost<=2:
		if structure is not None:
			t = structure.shape[0]//2
			if t > fakeGhost:
				fakeGhost = t
		
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="black_tophat",operationArgumentDic=operationArgumentDic)
	return v.main()

def grey_dilation(input,blockSize=50,fakeGhost=1,makeFloat32=True,size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):

	if fakeGhost<=1:
		if structure is not None:
			fakeGhost = structure.shape[0]//2
	operationArgumentDic = {"size":size,"footprint":footprint,"structure":structure,"output":output,"mode":mode,"cval":cval,"origin":origin}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="grey_dilation",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def grey_erosion(input,blockSize=50,fakeGhost=1,makeFloat32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):

	if fakeGhost<=1:
		if structure is not None:
			fakeGhost = structure.shape[0]//2
		
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="grey_erosion",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def grey_closing(input,blockSize=50,fakeGhost=2,makeFloat32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):

	if fakeGhost<=2:
		if structure is not None:
			t = structure.shape[0]//2
			if t > fakeGhost:
				fakeGhost = t
		
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="grey_closing",operationArgumentDic=operationArgumentDic)
	return v.main()
	

	
def grey_opening(input,blockSize=50,fakeGhost=2,makeFloat32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):

	if fakeGhost<=2:
		if structure is not None:
			t = structure.shape[0]//2
			if t > fakeGhost:
				fakeGhost = t
		
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="grey_opening",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def morphological_gradient(input,blockSize=50,fakeGhost=1,makeFloat32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	
	if fakeGhost<=1:
		if structure is not None:
			fakeGhost = structure.shape[0]//2
		
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="morphological_gradient",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def morphological_laplace(input,blockSize=50,fakeGhost=1,makeFloat32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	
	if fakeGhost<=1:
		if structure is not None:
			fakeGhost = structure.shape[0]//2
		
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="morphological_laplace",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def white_tophat(input,blockSize=50,fakeGhost=2,makeFloat32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):

	if fakeGhost<=2:
		if structure is not None:
			t = structure.shape[0]//2
			if t > fakeGhost:
				fakeGhost = t
		
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="white_tophat",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def intMultiply(input,blockSize=50,fakeGhost=1,makeFloat32=True,scalar=1):
	
	operationArgumentDic = {"scalar":scalar}
	v = VoxelProcessing(input,blockSize,fakeGhost,makeFloat32,operation="intMultiply",operationArgumentDic=operationArgumentDic)
	return v.main()
	
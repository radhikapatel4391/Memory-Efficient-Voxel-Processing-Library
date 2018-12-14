from voxelProcessing import VoxelProcessing
import numpy as np
'''
Prerequisite
numpy 
scipy
How to use this module

Example: 
	import voxel as vc
	output = vc.grey_dilation(input_var,structure=structure,no_of_blocks=7,fakeghost=4,make_float32=False)
	
	here,input_var = numpy 3d array
		structure = structure you want to use for morphological operation.
		no_of_blocks = how many blocks(frame with respect to x axis) you want to make of original image. default:4 
		fakeghost = extra border arround each block, generally proposnal to structuring element. default:1 or 2 
		make_float32 = True/False , do you want to type casting to float32? default:True

This module provide total 16 different operation, first 14 operation are same as ,

1 binary_dilation()
2 binary_erosion()
3 binary_closing()
4 binary_opening()
5 binary_hit_or_miss()
6 binary_propagation()
7 binary_fill_holes()
8 black_tophat()
9 grey_dilation()
10 grey_erosion()
11 grey_closing()
12 grey_opening()
13 morphological_gradient()
14 morphological_laplace()
15 white_tophat()
16 multiply() (integer/float valut multiplication with each element.)
17 nothing() (not perform any operation just do blocking and merging.)

'''


def binary_dilation(input_var,no_of_blocks=4,fakeghost=1,make_float32=True, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False):
	'''
	 overload of binary_dilation methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	if fakeghost<=1:
		if structure is not None:
			fakeghost = structure.shape[0]//2
		
	operationArgumentDic = {"structure":structure,"iterations":iterations,"output":output,"origin":origin,"mask":mask, "border_value":border_value, "brute_force":brute_force}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="binary_dilation",operationArgumentDic=operationArgumentDic)
	return v.main()	
	
def binary_erosion(input_var,no_of_blocks=4,fakeghost=1,make_float32=True, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False):
	'''
	 overload of binary_erosion methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	if fakeghost<=1:
		if structure is not None:
			fakeghost = structure.shape[0]//2
		
	operationArgumentDic = {"structure":structure,"iterations":iterations,"output":output,"origin":origin,"mask":mask, "border_value":border_value, "brute_force":brute_force}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="binary_erosion",operationArgumentDic=operationArgumentDic)
	return v.main()		

def binary_closing(input_var,no_of_blocks=4,fakeghost=2,make_float32=True, structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False):
	'''
	 overload of binary_closing methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
	if fakeghost<=2:
		if structure is not None:
			fakeghost = structure.shape[0]//2
	if  fakeghost<2:
		fakeghost = 2
		
	operationArgumentDic = {"structure":structure,"iterations":iterations,"output":output,"origin":origin,"mask":mask, "border_value":border_value, "brute_force":brute_force}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="binary_closing",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def binary_opening(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False):
	'''
	 overload of binary_opening methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
	if fakeghost<=2:
		if structure is not None:
			fakeghost = structure.shape[0]//2
			
	if  fakeghost<2:
		fakeghost = 2
	operationArgumentDic = {"structure":structure,"iterations":iterations,"output":output,"origin":origin,"mask":mask, "border_value":border_value, "brute_force":brute_force}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="binary_opening",operationArgumentDic=operationArgumentDic)
	return v.main()	
	

'''
you can't perform this operation locally need information of whole image...so result might be wrong....
'''	
def binary_fill_holes(input_var,no_of_blocks=4,fakeghost=1,make_float32=True, structure=None, output=None, origin=0):
	'''
	 overload of binary_fill_holes methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	if fakeghost<=1:
		if structure is not None:
			fakeghost = structure.shape[0]//2
		
	operationArgumentDic = {"structure":structure,"output":output,"origin":origin}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="binary_fill_holes",operationArgumentDic=operationArgumentDic)
	return v.main()	
	
def binary_hit_or_miss(input_var, no_of_blocks=4,fakeghost=1,make_float32=True, structure1=None, structure2=None, output=None, origin1=0, origin2=None):
	'''
	 overload of binary_hit_or_miss methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	if fakeghost<=1:
		if structure1 is not None:
			fakeghost = structure1.shape[0]//2
		
	operationArgumentDic = {"structure1":structure1,"structure2":structure2,"output":output,"origin1":origin1,"origin2":origin2}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="binary_hit_or_miss",operationArgumentDic=operationArgumentDic)
	return v.main()
	

def binary_propagation(input_var,no_of_blocks=4,fakeghost=1,make_float32=True, structure=None, mask=None, output=None, border_value=0, origin=0):
	'''
	 overload of binary_propagation methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	if fakeghost<=1:
		if structure is not None:
			fakeghost = structure.shape[0]//2
		
	operationArgumentDic = {"structure":structure,"output":output,"origin":origin,"mask":mask, "border_value":border_value}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="binary_propagation",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def black_tophat(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of black_tophat methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
	if fakeghost<=2:
		if structure is not None:
			fakeghost = structure.shape[0]//2
			
	if  fakeghost<2:
		fakeghost = 2	
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="black_tophat",operationArgumentDic=operationArgumentDic)
	return v.main()

def grey_dilation(input_var,no_of_blocks=4,fakeghost=1,make_float32=True,size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of grey_dilation methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	if fakeghost<=1:
		if structure is not None:
			fakeghost = structure.shape[0]//2
	operationArgumentDic = {"size":size,"footprint":footprint,"structure":structure,"output":output,"mode":mode,"cval":cval,"origin":origin}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="grey_dilation",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def grey_erosion(input_var,no_of_blocks=4,fakeghost=1,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of grey_erosion methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	if fakeghost<=1:
		if structure is not None:
			fakeghost = structure.shape[0]//2
		
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="grey_erosion",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def grey_closing(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of grey_closing methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
	if fakeghost<=2:
		if structure is not None:
			fakeghost = structure.shape[0]//2
			
	if  fakeghost<2:
		fakeghost = 2	
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="grey_closing",operationArgumentDic=operationArgumentDic)
	return v.main()
	

	
def grey_opening(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of grey_opening methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
	if fakeghost<=2:
		if structure is not None:
			fakeghost = structure.shape[0]//2
			
	if  fakeghost<2:
		fakeghost = 2	
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="grey_opening",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def morphological_gradient(input_var,no_of_blocks=4,fakeghost=1,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of morphological_gradient methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	if fakeghost<=1:
		if structure is not None:
			fakeghost = structure.shape[0]//2
		
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="morphological_gradient",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def morphological_laplace(input_var,no_of_blocks=4,fakeghost=1,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of morphological_laplace methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	if fakeghost<=1:
		if structure is not None:
			fakeghost = structure.shape[0]//2
		
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="morphological_laplace",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def white_tophat(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of white_tophat methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
	if fakeghost<=2:
		if structure is not None:
			fakeghost = structure.shape[0]//2
	if  fakeghost<2:
		fakeghost = 2
		
	operationArgumentDic = {"size":size, "footprint":footprint, "structure":structure, "output":output, "mode":mode, "cval":cval, "origin":origin}	
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="white_tophat",operationArgumentDic=operationArgumentDic)
	return v.main()
	
def multiply(input_var,no_of_blocks=4,fakeghost=1,make_float32=True,scalar=1):
	'''
	return multiplication of each value in matrix with given scalar integer.
	Parameters
	----------        
	scalar : int/float value with you want to do matrix multiplication. 
	'''
	operationArgumentDic = {"scalar":scalar}
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32,operation="multiply",operationArgumentDic=operationArgumentDic)
	return v.main()

#Not doing  any operation ...	
def nothing(input_var,no_of_blocks=4,fakeghost=1,make_float32=True):
	'''
	for algorithm testing purpose to make sure blocking and retriving stored output work as expected if output is same as input.
	Parameters
	----------
	input_var       : type: 3D numpy array
	no_of_blocks    : type: int, number of frame(block) you want in input array with respect to x axis. ex = 4
	fakeghost       : type: int, extra border around block, generally with respect to structure element size. ex = 1
	make_float32    : type: boolean, do you want to type cast input numpy array to float32.
	
	Returns
	-------
	output          : 3d numpy array, same as input.
	'''
	v = VoxelProcessing(input_var,no_of_blocks,fakeghost,make_float32)
	return v.main()
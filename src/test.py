import voxel as vc
from scipy.sparse import random
import time as t
import numpy as np
from scipy import ndimage
import os
import unittest
'''
test script which perform all  operation to check all operation provided by module working as expected or not.
It prints time taken by default scipy module and using our approach.

Golab variable creation for testing.....
PL = parameter list, no_of_blocks=PL[0],fakeghost=PL[1] 
input_svar = To test sparsed method generate Global sparse array,  with 0.3 desity of size 400x400x400.
input_svar = To test dense method generate Global dense array, input_dvar, with 0.7 desity of size 400x400x400.

Note : did Globaly over setUp() and tearDown() because input array creation take more time then performing operation plus we have no need of creation before each testing operation.

No of tests
Sparse Input - test_sparse_operation()
	- Different no_of_blocks               -  __test_blocks()
	- Different fakeghostSize              -  __test_fakeghost()
	- make_float32_True - which is default -  __test_nothing_make_float32_True()
	
Dense Input - test_dense_operation()
	- Different no_of_blocks               -  __test_blocks()
	- Different fakeghostSize              -  __test_fakeghost()
	- make_float32_True - which is default -  __test_nothing_make_float32_True()
	
		each of three call this methods,
			1__test_binary_dilation_operation()
			2__test_binary_erosion_operation()
			3__test_binary_closing_operation()
			4__test_binary_opening_operation()
			5__test_binary_hit_or_miss_operation()
			6__test_binary_propagation_operation()
			7__test_binary_fill_holes_operation()
			8__test_black_tophat_operation()
			9__test_grey_dilation_operation()
			10__test_grey_erosion_operation()
			11__test_grey_closing_operation()
			12__test_grey_opening_operation()
			13__test_morphological_gradient_operation()
			14__test_morphological_laplace_operation()
			15__test_white_tophat_operation()
			16__test_multiply_operation()
			17__test_nothing_operation()
			

'''

PL=[4,1] #no_of_blocks=PL[0],fakeghost=PL[1]
print("creating dense input array will take time...")
structure = np.ones((3,3,3))
input_dvar = random(400,160000,density=0.7,dtype="float64")
input_dvar = input_dvar.todense()
input_dvar = np.array(input_dvar)
input_dvar = np.reshape(input_dvar,(400,400,400))

# creating sparse input array
print("creating sparse input array will take time...")
input_svar = random(400,160000,density=0.3,dtype="float64")
input_svar = input_svar.todense()
input_svar = np.array(input_svar)
input_svar = np.reshape(input_svar,(400,400,400))

class WidgetTestCase(unittest.TestCase):

	def test_sparse_operation(self):
		self.__test_blocks(input_svar)
		self.__test_fakeghost(input_svar)
		self.__test_nothing_make_float32_True(input_svar)
		
	def test_dense_operation(self):
		self.__test_blocks(input_dvar)
		self.__test_fakeghost(input_dvar)
		self.__test_nothing_make_float32_True(input_dvar)
		
	def __test_blocks(self,input_var):
		temp = [4,7]
		for i in temp:
			PL[0] = i				
			self.__test_all_operation(input_var)
		PL[0] = 4
			
	def __test_fakeghost(self,input_var):
		temp = [1,2,7]
		for i in temp:
			PL[1] = i				
			self.__test_all_operation(input_var)
		PL[1]=2
	
	def __test_nothing_make_float32_True(self,input_var):
		print("\n nothing testing...")
		start_time = t.time()
		v_output = vc.nothing(input_var,no_of_blocks=PL[0],fakeghost=PL[1])
		print("vc nothing time taken: ",(t.time() - start_time)," sec")
		msgs = "nothing_operation_fail_with parameters: make_float32=True"		
		self.assertFalse((input_var==v_output).all(), msg=msgs)
		self.assertTrue((v_output.dtype=="float32"), msg="data type is not converted to float32")	
		
	def __test_all_operation(self,input_var):
		self.__test_binary_dilation_operation(input_var)
		self.__test_binary_erosion_operation(input_var)
		self.__test_binary_closing_operation(input_var)
		self.__test_binary_opening_operation(input_var)
		self.__test_binary_hit_or_miss_operation(input_var)
		self.__test_binary_propagation_operation(input_var)
		self.__test_black_tophat_operation(input_var)
		self.__test_grey_dilation_operation(input_var)
		self.__test_grey_erosion_operation(input_var)
		self.__test_grey_closing_operation(input_var)
		self.__test_grey_opening_operation(input_var)
		self.__test_morphological_gradient_operation(input_var)
		self.__test_morphological_laplace_operation(input_var)
		self.__test_white_tophat_operation(input_var)
		self.__test_binary_fill_holes_operation(input_var)
		self.__test_multiply_operation(input_var)
		self.__test_nothing_operation(input_var)	

	def __test_binary_dilation_operation(self,input_var):		
		print("\n binary_dilation Voxel testing...")
		start_time = t.time()
		v_output = vc.binary_dilation(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("binary_dilation Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n binary_dilation Default testing...")
		start_time = t.time()
		d_output = ndimage.binary_dilation(input_var,structure=structure)
		print("binary_dilation Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "binary_dilation_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="binary_dilation_operation_FAIL_with_output type")
		
	def __test_binary_erosion_operation(self,input_var):		
		print("\n binary_erosion Voxel testing...")
		start_time = t.time()
		v_output = vc.binary_erosion(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("binary_erosion Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n binary_erosion Default testing...")
		start_time = t.time()
		d_output = ndimage.binary_erosion(input_var,structure=structure)
		print("binary_erosion Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "binary_erosion_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="binary_erosion_operation_FAIL_with_output type")
		
	def __test_binary_closing_operation(self,input_var):		
		print("\n binary_closing Voxel testing...")
		start_time = t.time()
		v_output = vc.binary_closing(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("binary_closing Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n binary_closing Default testing...")
		start_time = t.time()
		d_output = ndimage.binary_closing(input_var,structure=structure)
		print("binary_closing Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "binary_closing_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="binary_closing_operation_FAIL_with_output type")
		
	def __test_binary_opening_operation(self,input_var):		
		print("\n binary_opening Voxel testing...")
		start_time = t.time()
		v_output = vc.binary_opening(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("binary_opening Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n binary_opening Default testing...")
		start_time = t.time()
		d_output = ndimage.binary_opening(input_var,structure=structure)
		print("binary_opening Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "binary_opening_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="binary_opening_operation_FAIL_with_output type")
		
	def __test_binary_hit_or_miss_operation(self,input_var):		
		print("\n binary_hit_or_miss Voxel testing...")
		start_time = t.time()
		v_output = vc.binary_hit_or_miss(input_var,structure1=structure,structure2=None,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("binary_hit_or_miss Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n binary_hit_or_miss Default testing...")
		start_time = t.time()
		d_output = ndimage.binary_hit_or_miss(input_var,structure1=structure, structure2=None,)
		print("binary_hit_or_miss Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "binary_hit_or_miss_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="binary_hit_or_miss_operation_FAIL_with_output type")
		
	def __test_binary_propagation_operation(self,input_var):		
		print("\n binary_propagation Voxel testing...")
		start_time = t.time()
		v_output = vc.binary_propagation(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("binary_propagation Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n binary_propagation Default testing...")
		start_time = t.time()
		d_output = ndimage.binary_propagation(input_var,structure=structure)
		print("binary_propagation Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "binary_propagation_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="binary_propagation_operation_FAIL_with_output type")
		
	def __test_black_tophat_operation(self,input_var):		
		print("\n black_tophat Voxel testing...")
		start_time = t.time()
		v_output = vc.black_tophat(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("black_tophat Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n black_tophat Default testing...")
		start_time = t.time()
		d_output = ndimage.black_tophat(input_var,structure=structure)
		print("black_tophat Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "black_tophat_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="black_tophat_operation_FAIL_with_output type")
		
	def __test_grey_dilation_operation(self,input_var):		
		print("\n grey_dilation Voxel testing...")
		start_time = t.time()
		v_output = vc.grey_dilation(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("grey_dilation Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n grey_dilation Default testing...")
		start_time = t.time()
		d_output = ndimage.grey_dilation(input_var,structure=structure)
		print("grey_dilation Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "grey_dilation_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="grey_dilation_operation_FAIL_with_output type")
		
	def __test_grey_erosion_operation(self,input_var):		
		print("\n grey_erosion Voxel testing...")
		start_time = t.time()
		v_output = vc.grey_erosion(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("grey_erosion Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n grey_erosion Default testing...")
		start_time = t.time()
		d_output = ndimage.grey_erosion(input_var,structure=structure)
		print("grey_erosion Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "grey_erosion_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="grey_erosion_operation_FAIL_with_output type")
		
	def __test_grey_closing_operation(self,input_var):		
		print("\n grey_closing Voxel testing...")
		start_time = t.time()
		v_output = vc.grey_closing(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("grey_closing Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n grey_closing Default testing...")
		start_time = t.time()
		d_output = ndimage.grey_closing(input_var,structure=structure)
		print("grey_closing Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "grey_closing_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="grey_closing_operation_FAIL_with_output type")
		
	def __test_grey_opening_operation(self,input_var):		
		print("\n grey_opening Voxel testing...")
		start_time = t.time()
		v_output = vc.grey_opening(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("grey_opening Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n grey_opening Default testing...")
		start_time = t.time()
		d_output = ndimage.grey_opening(input_var,structure=structure)
		print("grey_opening Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "grey_opening_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="grey_opening_operation_FAIL_with_output type")
		
	def __test_morphological_gradient_operation(self,input_var):		
		print("\n morphological_gradient Voxel testing...")
		start_time = t.time()
		v_output = vc.morphological_gradient(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("morphological_gradient Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n morphological_gradient Default testing...")
		start_time = t.time()
		d_output = ndimage.morphological_gradient(input_var,structure=structure)
		print("morphological_gradient Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "morphological_gradient_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="morphological_gradient_operation_FAIL_with_output type")
		
	def __test_morphological_laplace_operation(self,input_var):		
		print("\n morphological_laplace Voxel testing...")
		start_time = t.time()
		v_output = vc.morphological_laplace(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("morphological_laplace Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n morphological_laplace Default testing...")
		start_time = t.time()
		d_output = ndimage.morphological_laplace(input_var,structure=structure)
		print("morphological_laplace Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "morphological_laplace_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="morphological_laplace_operation_FAIL_with_output type")
		
	def __test_white_tophat_operation(self,input_var):		
		print("\n white_tophat Voxel testing...")
		start_time = t.time()
		v_output = vc.white_tophat(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("white_tophat Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n white_tophat Default testing...")
		start_time = t.time()
		d_output = ndimage.white_tophat(input_var,structure=structure)
		print("white_tophat Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "white_tophat_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="white_tophat_operation_FAIL_with_output type")
		
	def __test_binary_fill_holes_operation(self,input_var):		
		print("\n binary_fill_holes Voxel testing...")
		start_time = t.time()
		v_output = vc.binary_fill_holes(input_var,structure=structure,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("binary_fill_holes Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n binary_fill_holes Default testing...")
		start_time = t.time()
		d_output = ndimage.binary_fill_holes(input_var,structure=structure)
		print("binary_fill_holes Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "binary_fill_holes_operation_FAIL_with parameters: ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="binary_fill_holes_operation_FAIL_with_output type")
		
	def __test_multiply_operation(self,input_var):		
		print("\n multiply Voxel testing...")
		start_time = t.time()
		v_output = vc.multiply(input_var,scalar=5,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("multiply Voxel testing time taken: ",(t.time() - start_time)," sec")
		#print("\n multiply Default testing...")
		start_time = t.time()
		d_output = input_var*5
		print("multiply Default testing time taken: ",(t.time() - start_time)," sec")		
		msgs = "multiply_operation_FAIL_with parameters: scalar=5, ",PL
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		#self.assertTrue((d_output.dtype==v_output.dtype), msg="multiply_operation_FAIL_with_output type"	
		
	def __test_nothing_operation(self,input_var):		
		print("\n nothing testing...")
		start_time = t.time()
		v_output = vc.nothing(input_var,no_of_blocks=PL[0],fakeghost=PL[1],make_float32=False)
		print("vc nothing time taken: ",(t.time() - start_time)," sec")
		msgs = "nothing_operation_fail_with parameters: ",PL		
		self.assertTrue((input_var==v_output).all(), msg=msgs)
		
	
if __name__ == '__main__':
    unittest.main()


'''with out unit testing usage demo.. 
output = vc.grey_dilation(input_var,structure=structure,no_of_blocks=6,fakeghost=4,make_float32=False)

'''
'''
print("creating dense input array will take time...")
structure = np.ones((3,3,3))
input_var = random(400,160000,density=0.7,dtype="float64")
input_var = input_var.todense()
input_var = np.array(input_var)
input_var = np.reshape(input_var,(400,400,400))
print("..............................dense operation testing..............................................")
#5.binary_closing..............
print("\nbinary_closing VoxelProcessing")
start_time = t.time()
output = vc.binary_closing(input_var,make_float32=False,structure=structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("vc binary_closing: ",(t.time() - start_time)," sec")
print("\nbinary_closing Default")
start_time = t.time()
d = ndimage.binary_closing(input_var,structure=structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("scipy binary_closing: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#6.binary_opening..............
print("\nbinary_opening VoxelProcessing")
start_time = t.time()
output = vc.binary_opening(input_var, structure=structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("vc binary_opening: ",(t.time() - start_time)," sec")
print("\nbinary_opening Default")
start_time = t.time()
d = ndimage.binary_opening(input_var, structure=structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("scipy binary_opening: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#0.Nothing..............
print("\n nothing testing...")
start_time = t.time()
output = vc.nothing(input_var,no_of_blocks=7,fakeghost=4,make_float32=False)
print("vc nothing: ",(t.time() - start_time)," sec")
print("\nresult: ",(input_var==output).all())

#1.grey_dilation..............
print("\ngrey_dilation VoxelProcessing")
start_time = t.time()
output = vc.grey_dilation(input_var,no_of_blocks=6,structure=structure,make_float32=False)
print("vc grey_dilation: ",(t.time() - start_time)," sec")
print("\ngrey_dilation Default")
start_time = t.time()
d = ndimage.grey_dilation(input_var,structure=structure)
print("scipy grey_dilation: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#2.grey_erosion..............
print("\ngrey_erosion VoxelProcessing")
start_time = t.time()
output = vc.grey_erosion(input_var,no_of_blocks=7, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc grey_erosion: ",(t.time() - start_time)," sec")
print("\ngrey_erosion Default")
start_time = t.time()
d = ndimage.grey_erosion(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy grey_erosion: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#3.grey_closing..............
print("\ngrey_closing VoxelProcessing")
start_time = t.time()
output = vc.grey_closing(input_var,make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc grey_closing: ",(t.time() - start_time)," sec")
print("\ngrey_closing Default")
start_time = t.time()
d = ndimage.grey_closing(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy grey_closing: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#4.grey_opening..............
print("\ngrey_opening VoxelProcessing")
start_time = t.time()
output = vc.grey_opening(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc grey_opening: ",(t.time() - start_time)," sec")
print("\ngrey_opening Default")
start_time = t.time()
d = ndimage.grey_opening(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy grey_opening: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#7.binary_dilation..............

#8.binary_erosion..............
print("\nbinary_erosion VoxelProcessing")
start_time = t.time()
output = vc.binary_erosion(input_var, make_float32=False,structure=structure,iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("vc binary_erosion: ",(t.time() - start_time)," sec")
print("\nbinary_erosion Default")
start_time = t.time()
d = ndimage.binary_erosion(input_var, structure=structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("scipy binary_erosion: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#10.binary_hit_or_miss..............
print("\nbinary_hit_or_miss VoxelProcessing")
start_time = t.time()
output = vc.binary_hit_or_miss(input_var, make_float32=False,  structure1=structure, structure2=None, output=None, origin1=0, origin2=None)
print("vc binary_hit_or_miss: ",(t.time() - start_time)," sec")
print("\nbinary_hit_or_miss Default")
start_time = t.time()
d = ndimage.binary_hit_or_miss(input_var, structure1=structure, structure2=None, output=None, origin1=0, origin2=None)
print("scipy binary_hit_or_miss: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#11.binary_propagation..............
print("\nbinary_propagation VoxelProcessing")
start_time = t.time()
output = vc.binary_propagation(input_var, make_float32=False,  structure=structure, mask=None, output=None, border_value=0, origin=0)
print("vc binary_propagation: ",(t.time() - start_time)," sec")
print("\nbinary_propagation Default")
start_time = t.time()
d = ndimage.binary_propagation(input_var, structure=structure, mask=None, output=None, border_value=0, origin=0)
print("scipy binary_propagation: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#12.black_tophat..............
print("\nblack_tophat VoxelProcessing")
start_time = t.time()
output = vc.black_tophat(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc black_tophat: ",(t.time() - start_time)," sec")
print("\nblack_tophat Default")
start_time = t.time()
d = ndimage.black_tophat(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy black_tophat: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#13.morphological_gradient..............
print("\nmorphological_gradient VoxelProcessing")
start_time = t.time()
output = vc.morphological_gradient(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc morphological_gradient: ",(t.time() - start_time)," sec")
print("\nmorphological_gradient Default")
start_time = t.time()
d = ndimage.morphological_gradient(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy morphological_gradient: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#14.morphological_laplace..............
print("\nmorphological_laplace VoxelProcessing")
start_time = t.time()
output = vc.morphological_laplace(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc morphological_laplace: ",(t.time() - start_time)," sec")
print("\nmorphological_laplace Default")
start_time = t.time()
d = ndimage.morphological_laplace(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy morphological_laplace: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#15.white_tophat..............
print("\nwhite_tophat VoxelProcessing")
start_time = t.time()
output = vc.white_tophat(input_var, make_float32=False, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc white_tophat: ",(t.time() - start_time)," sec")
print("\nwhite_tophat VoxelProcessing Default")
start_time = t.time()
d = ndimage.white_tophat(input_var,size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy white_tophat: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#16.multiply..............
print("\nmultiply VoxelProcessing")
start_time = t.time()
output = vc.multiply(input_var, make_float32=False, no_of_blocks=7,fakeghost=1,scalar=10)
print("vc multiply: ",(t.time() - start_time)," sec")
print("\nmultiply Default")
start_time = t.time()
d = input_var*10
print("scipy multiply: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())




print("creating dense input array will take time...")
structure = np.ones((3,3,3))
input_var = random(400,160000,density=0.3,dtype="float64")
input_var = input_var.todense()
input_var = np.array(input_var)
input_var = np.reshape(input_var,(400,400,400))

#input_var = np.load("400_400_400_0.3.npy", mmap_mode="r")

print("..............................Sparse operation testing..............................................")

#5.binary_closing..............
print("\nbinary_closing VoxelProcessing")
start_time = t.time()
output = vc.binary_closing(input_var,make_float32=False,structure=structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("vc binary_closing: ",(t.time() - start_time)," sec")
print("\nbinary_closing Default")
start_time = t.time()
d = ndimage.binary_closing(input_var,structure=structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("scipy binary_closing: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#6.binary_opening..............
print("\nbinary_opening VoxelProcessing")
start_time = t.time()
output = vc.binary_opening(input_var, structure=structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("vc binary_opening: ",(t.time() - start_time)," sec")
print("\nbinary_opening Default")
start_time = t.time()
d = ndimage.binary_opening(input_var, structure=structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("scipy binary_opening: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#0.Nothing..............
print("\n nothing testing...")
start_time = t.time()
output = vc.nothing(input_var,no_of_blocks=7,fakeghost=4,make_float32=False)
print("vc nothing: ",(t.time() - start_time)," sec")
print("\nresult: ",(input_var==output).all())

#1.grey_dilation..............
print("\ngrey_dilation VoxelProcessing")
start_time = t.time()
output = vc.grey_dilation(input_var,no_of_blocks=6,structure=structure,make_float32=False)
print("vc grey_dilation: ",(t.time() - start_time)," sec")
print("\ngrey_dilation Default")
start_time = t.time()
d = ndimage.grey_dilation(input_var,structure=structure)
print("scipy grey_dilation: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#2.grey_erosion..............
print("\ngrey_erosion VoxelProcessing")
start_time = t.time()
output = vc.grey_erosion(input_var,no_of_blocks=7, make_float32=False,structure=structure)
print("vc grey_erosion: ",(t.time() - start_time)," sec")
print("\ngrey_erosion Default")
start_time = t.time()
d = ndimage.grey_erosion(input_var,structure=structure, )
print("scipy grey_erosion: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#3.grey_closing..............
print("\ngrey_closing VoxelProcessing")
start_time = t.time()
output = vc.grey_closing(input_var,make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc grey_closing: ",(t.time() - start_time)," sec")
print("\ngrey_closing Default")
start_time = t.time()
d = ndimage.grey_closing(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy grey_closing: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#4.grey_opening..............
print("\ngrey_opening VoxelProcessing")
start_time = t.time()
output = vc.grey_opening(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc grey_opening: ",(t.time() - start_time)," sec")
print("\ngrey_opening Default")
start_time = t.time()
d = ndimage.grey_opening(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy grey_opening: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())



#7.binary_dilation..............
print("\nbinary_dilation VoxelProcessing")
start_time = t.time()
output = vc.binary_dilation(input_var,make_float32=False,  structure=structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("vc binary_dilation: ",(t.time() - start_time)," sec")
print("\nbinary_dilation Default")
start_time = t.time()
d = ndimage.binary_dilation(input_var, structure=structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("scipy binary_dilation: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#8.binary_erosion..............
print("\nbinary_erosion VoxelProcessing")
start_time = t.time()
output = vc.binary_erosion(input_var, make_float32=False,  structure=structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("vc binary_erosion: ",(t.time() - start_time)," sec")
print("\nbinary_erosion Default")
start_time = t.time()
d = ndimage.binary_erosion(input_var, structure=structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("scipy binary_erosion: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())



#10.binary_hit_or_miss..............
print("\nbinary_hit_or_miss VoxelProcessing")
start_time = t.time()
output = vc.binary_hit_or_miss(input_var, make_float32=False,  structure1=structure, structure2=None, output=None, origin1=0, origin2=None)
print("vc binary_hit_or_miss: ",(t.time() - start_time)," sec")
print("\nbinary_hit_or_miss Default")
start_time = t.time()
d = ndimage.binary_hit_or_miss(input_var, structure1=structure, structure2=None, output=None, origin1=0, origin2=None)
print("scipy binary_hit_or_miss: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#11.binary_propagation..............
print("\nbinary_propagation VoxelProcessing")
start_time = t.time()
output = vc.binary_propagation(input_var, make_float32=False,  structure=structure, mask=None, output=None, border_value=0, origin=0)
print("vc binary_propagation: ",(t.time() - start_time)," sec")
print("\nbinary_propagation Default")
start_time = t.time()
d = ndimage.binary_propagation(input_var, structure=structure, mask=None, output=None, border_value=0, origin=0)
print("scipy binary_propagation: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#12.black_tophat..............
print("\nblack_tophat VoxelProcessing")
start_time = t.time()
output = vc.black_tophat(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc black_tophat: ",(t.time() - start_time)," sec")
print("\nblack_tophat Default")
start_time = t.time()
d = ndimage.black_tophat(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy black_tophat: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#13.morphological_gradient..............
print("\nmorphological_gradient VoxelProcessing")
start_time = t.time()
output = vc.morphological_gradient(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc morphological_gradient: ",(t.time() - start_time)," sec")
print("\nmorphological_gradient Default")
start_time = t.time()
d = ndimage.morphological_gradient(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy morphological_gradient: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#14.morphological_laplace..............
print("\nmorphological_laplace VoxelProcessing")
start_time = t.time()
output = vc.morphological_laplace(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc morphological_laplace: ",(t.time() - start_time)," sec")
print("\nmorphological_laplace Default")
start_time = t.time()
d = ndimage.morphological_laplace(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy morphological_laplace: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#15.white_tophat..............
print("\nwhite_tophat VoxelProcessing")
start_time = t.time()
output = vc.white_tophat(input_var, make_float32=False, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc white_tophat: ",(t.time() - start_time)," sec")
print("\nwhite_tophat VoxelProcessing Default")
start_time = t.time()
d = ndimage.white_tophat(input_var,size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy white_tophat: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#16.multiply..............
print("\nmultiply VoxelProcessing")
start_time = t.time()
output = vc.multiply(input_var, make_float32=False, no_of_blocks=7,fakeghost=1,scalar=10)
print("vc multiply: ",(t.time() - start_time)," sec")
print("\nmultiply Default")
start_time = t.time()
d = input_var*10
print("scipy multiply: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())


# # print(output[134][156][98])
# # print(d[134][156][98])
# # t = np.setdiff1d(output, d)
# # print(len(t))
'''
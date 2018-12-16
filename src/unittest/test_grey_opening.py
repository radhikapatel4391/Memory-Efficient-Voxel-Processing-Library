'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
from scipy.sparse import random
import time as t
import numpy as np
from scipy import ndimage
import os,sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("voxel.py"))))
import voxel as vc

structure = ndimage.generate_binary_structure(3, 1) #np.ones((3,3,3))
try:
	input_dvar = np.load("dense_array.npy", mmap_mode="r")
except:	
	print("creating dense input array will take time...")	
	input_dvar = random(400,160000,density=0.7,dtype="float64")
	input_dvar = input_dvar.todense()
	input_dvar = np.array(input_dvar)
	input_dvar = np.reshape(input_dvar,(400,400,400))
	np.save("dense_array.npy", input_dvar)

# creating sparse input array
try:
	input_svar = np.load("sparse_array.npy", mmap_mode="r")
except:
	print("creating sparse input array will take time...")
	input_svar = random(400,160000,density=0.3,dtype="float64")
	input_svar = input_svar.todense()
	input_svar = np.array(input_svar)
	input_svar = np.reshape(input_svar,(400,400,400))
	np.save("sparse_array.npy", input_svar)
	
class TestGreyOpening(unittest.TestCase):

	def test_grey_opening_operation_sparse_input_default_value(self):		
		print("\n test_grey_opening_operation_sparse_input_default_value...")		
		v_output = vc.grey_opening(input_svar, structure=structure, make_float32=False)		
		d_output = ndimage.grey_opening(input_svar, structure=structure,)			
		msgs = "test_grey_opening_operation_sparse_input_default_value"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_grey_opening_operation_sparse_input_struct_ones(self):
		struct = np.ones((3,3,3))
		print("\n test_grey_opening_operation_sparse_input_struct_ones...")		
		v_output = vc.grey_opening(input_svar, structure=struct,make_float32=False)		
		d_output = ndimage.grey_opening(input_svar, structure=struct)			
		msgs = "test_grey_opening_operation_sparse_input_struct_ones"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_grey_opening_operation_sparse_input_struct_zeros(self):
		struct = np.zeros((3,3,3))
		print("\n test_grey_opening_operation_sparse_input_struct_zeros...")		
		v_output = vc.grey_opening(input_svar, structure=struct,make_float32=False)		
		d_output = ndimage.grey_opening(input_svar, structure=struct)			
		msgs = "test_grey_opening_operation_sparse_input_struct_zeros"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_grey_opening_operation_sparse_input_blocks_two(self):		
		print("\n test_grey_opening_operation_sparse_input_blocks_two...")		
		v_output = vc.grey_opening(input_svar, structure=structure, no_of_blocks=2,make_float32=False)		
		d_output = ndimage.grey_opening(input_svar, structure=structure,)			
		msgs = "test_grey_opening_operation_sparse_input_blocks_two"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_grey_opening_operation_sparse_input_blocks_ten(self):		
		print("\n test_grey_opening_operation_sparse_input_blocks_ten...")		
		v_output = vc.grey_opening(input_svar, structure=structure, no_of_blocks=10,make_float32=False)		
		d_output = ndimage.grey_opening(input_svar, structure=structure,)			
		msgs = "test_grey_opening_operation_sparse_input_blocks_ten"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_grey_opening_operation_sparse_input_fakeghost_one(self):		
		print("\n test_grey_opening_operation_sparse_input_fakeghost_one...")		
		v_output = vc.grey_opening(input_svar, structure=structure, fakeghost=1,make_float32=False)		
		d_output = ndimage.grey_opening(input_svar, structure=structure,)			
		msgs = "test_grey_opening_operation_sparse_input_fakeghost_one"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_grey_opening_operation_sparse_input_fakeghost_four(self):		
		print("\n test_grey_opening_operation_sparse_input_fakeghost_four...")		
		v_output = vc.grey_opening(input_svar,structure=structure, fakeghost=4,make_float32=False)		
		d_output = ndimage.grey_opening(input_svar,structure=structure,)			
		msgs = "test_grey_opening_operation_sparse_input_fakeghost_four"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	#not necessary output will be always different depen on input array values..	
	# def test_grey_opening_operation_sparse_input_make_float32_true(self):		
		# print("\n test_grey_opening_operation_sparse_input_make_float32_true...")		
		# v_output = vc.grey_opening(input_svar,structure=structure)		
		# d_output = ndimage.grey_opening(input_svar,structure=structure,)			
		# msgs = "test_grey_opening_operation_sparse_input_make_float32_true"
		# self.assertFalse((d_output==v_output).all(), msg=msgs)
	
#dense operation testing.........

	def test_grey_opening_operation_dense_input_default_value(self):		
		print("\n test_grey_opening_operation_dense_input_default_value...")		
		v_output = vc.grey_opening(input_dvar, structure=structure, make_float32=False)		
		d_output = ndimage.grey_opening(input_dvar, structure=structure,)			
		msgs = "test_grey_opening_operation_dense_input_default_value"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_grey_opening_operation_dense_input_struct_ones(self):
		struct = np.ones((3,3,3))
		print("\n test_grey_opening_operation_dense_input_struct_ones...")		
		v_output = vc.grey_opening(input_dvar, structure=struct,make_float32=False)		
		d_output = ndimage.grey_opening(input_dvar, structure=struct)			
		msgs = "test_grey_opening_operation_dense_input_struct_ones"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_grey_opening_operation_dense_input_struct_zeros(self):
		struct = np.zeros((3,3,3))
		print("\n test_grey_opening_operation_dense_input_struct_zeros...")		
		v_output = vc.grey_opening(input_dvar, structure=struct,make_float32=False)		
		d_output = ndimage.grey_opening(input_dvar, structure=struct)			
		msgs = "test_grey_opening_operation_dense_input_struct_zeros"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_grey_opening_operation_dense_input_blocks_two(self):		
		print("\n test_grey_opening_operation_dense_input_blocks_two...")		
		v_output = vc.grey_opening(input_dvar, structure=structure, no_of_blocks=2,make_float32=False)		
		d_output = ndimage.grey_opening(input_dvar, structure=structure,)			
		msgs = "test_grey_opening_operation_dense_input_blocks_two"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_grey_opening_operation_dense_input_blocks_ten(self):		
		print("\n test_grey_opening_operation_dense_input_blocks_ten...")		
		v_output = vc.grey_opening(input_dvar, structure=structure, no_of_blocks=10,make_float32=False)		
		d_output = ndimage.grey_opening(input_dvar, structure=structure,)			
		msgs = "test_grey_opening_operation_dense_input_blocks_ten"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_grey_opening_operation_dense_input_fakeghost_one(self):		
		print("\n test_grey_opening_operation_dense_input_fakeghost_one...")		
		v_output = vc.grey_opening(input_dvar, structure=structure, fakeghost=1,make_float32=False)		
		d_output = ndimage.grey_opening(input_dvar, structure=structure,)			
		msgs = "test_grey_opening_operation_dense_input_fakeghost_one"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_grey_opening_operation_dense_input_fakeghost_four(self):		
		print("\n test_grey_opening_operation_dense_input_fakeghost_four...")		
		v_output = vc.grey_opening(input_dvar,structure=structure, fakeghost=4,make_float32=False)		
		d_output = ndimage.grey_opening(input_dvar,structure=structure,)			
		msgs = "test_grey_opening_operation_dense_input_fakeghost_four"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	#not necessary output will be always different depen on input array values..	
	# def test_grey_opening_operation_dense_input_make_float32_true(self):		
		# print("\n test_grey_opening_operation_dense_input_make_float32_true...")		
		# v_output = vc.grey_opening(input_dvar,structure=structure)		
		# d_output = ndimage.grey_opening(input_dvar,structure=structure,)			
		# msgs = "test_grey_opening_operation_dense_input_make_float32_true"
		# self.assertFalse((d_output==v_output).all(), msg=msgs)
		
if __name__ == '__main__':
    unittest.main()
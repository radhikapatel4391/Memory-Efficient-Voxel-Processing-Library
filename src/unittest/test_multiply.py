from scipy.sparse import random
import time as t
import numpy as np
from scipy import ndimage
import os,sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("voxel.py"))))
import voxel as vc


try:
	input_dvar = np.load("dense_array.npy", mmap_mode="r")
except:	
	print("creating dense input array will take time...")
	structure = np.ones((3,3,3))
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
	
class TestMultiply(unittest.TestCase):

	def test_multiply_operation_sparse_input_default_value(self):		
		print("\n test_multiply_operation_sparse_input_default_value...")		
		v_output = vc.multiply(input_svar, scalar=5, make_float32=False)		
		d_output = input_svar*5			
		msgs = "test_multiply_operation_sparse_input_default_value"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_multiply_operation_sparse_input_scalar_float(self):		
		print("\n test_multiply_operation_sparse_input_scalar_float...")		
		v_output = vc.multiply(input_svar, scalar=5.5, make_float32=False)		
		d_output = input_svar*5.5		
		msgs = "test_multiply_operation_sparse_input_scalar_float"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
	
		
	def test_multiply_operation_sparse_input_blocks_two(self):		
		print("\n test_multiply_operation_sparse_input_blocks_two...")		
		v_output = vc.multiply(input_svar, scalar=5, no_of_blocks=2,make_float32=False)		
		d_output = input_svar*5						
		msgs = "test_multiply_operation_sparse_input_blocks_two"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_multiply_operation_sparse_input_blocks_ten(self):		
		print("\n test_multiply_operation_sparse_input_blocks_ten...")		
		v_output = vc.multiply(input_svar, scalar=5, no_of_blocks=10,make_float32=False)		
		d_output = input_svar*5			
		msgs = "test_multiply_operation_sparse_input_blocks_ten"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_multiply_operation_sparse_input_fakeghost_one(self):		
		print("\n test_multiply_operation_sparse_input_fakeghost_one...")		
		v_output = vc.multiply(input_svar, scalar=5, fakeghost=1,make_float32=False)		
		d_output = input_svar*5			
		msgs = "test_multiply_operation_sparse_input_fakeghost_one"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_multiply_operation_sparse_input_fakeghost_four(self):		
		print("\n test_multiply_operation_sparse_input_fakeghost_four...")		
		v_output = vc.multiply(input_svar,scalar=5, fakeghost=4,make_float32=False)		
		d_output = input_svar*5			
		msgs = "test_multiply_operation_sparse_input_fakeghost_four"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	#not necessary output will be always different depen on input array values..	
	# def test_multiply_operation_sparse_input_make_float32_true(self):		
		# print("\n test_multiply_operation_sparse_input_make_float32_true...")		
		# v_output = vc.multiply(input_svar,scalar=5)		
		# d_output = input_svar*5					
		# msgs = "test_multiply_operation_sparse_input_make_float32_true"
		# self.assertFalse((d_output==v_output).all(), msg=msgs)
	
#dense operation testing.........

	def test_multiply_operation_dense_input_default_value(self):		
		print("\n test_multiply_operation_dense_input_default_value...")		
		v_output = vc.multiply(input_dvar, scalar=5, make_float32=False)		
		d_output = input_dvar*5			
		msgs = "test_multiply_operation_dense_input_default_value"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	
		
	def test_multiply_operation_dense_input_blocks_two(self):		
		print("\n test_multiply_operation_dense_input_blocks_two...")		
		v_output = vc.multiply(input_dvar, scalar=5, no_of_blocks=2,make_float32=False)		
		d_output = input_dvar*5			
		msgs = "test_multiply_operation_dense_input_blocks_two"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_multiply_operation_dense_input_blocks_ten(self):		
		print("\n test_multiply_operation_dense_input_blocks_ten...")		
		v_output = vc.multiply(input_dvar, scalar=5, no_of_blocks=10,make_float32=False)		
		d_output = input_dvar*5			
		msgs = "test_multiply_operation_dense_input_blocks_ten"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_multiply_operation_dense_input_fakeghost_one(self):		
		print("\n test_multiply_operation_dense_input_fakeghost_one...")		
		v_output = vc.multiply(input_dvar, scalar=5, fakeghost=1,make_float32=False)		
		d_output = input_dvar*5			
		msgs = "test_multiply_operation_dense_input_fakeghost_one"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_multiply_operation_dense_input_fakeghost_four(self):		
		print("\n test_multiply_operation_dense_input_fakeghost_four...")		
		v_output = vc.multiply(input_dvar,scalar=5, fakeghost=4,make_float32=False)		
		d_output = input_dvar*5						
		msgs = "test_multiply_operation_dense_input_fakeghost_four"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	#not necessary output will be always different depen on input array values..	
	# def test_multiply_operation_dense_input_make_float32_true(self):		
		# print("\n test_multiply_operation_dense_input_make_float32_true...")		
		# v_output = vc.multiply(input_dvar,scalar=5)		
		# d_output = input_svar*5						
		# msgs = "test_multiply_operation_dense_input_make_float32_true"
		# self.assertFalse((d_output==v_output).all(), msg=msgs)
		
if __name__ == '__main__':
    unittest.main()
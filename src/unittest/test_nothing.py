'''
perform 5 (total 10) diffrent test on sparse and dense input array
1)_default_value: make_float32=False,no_of_blocks=4,fakeghost=2 default make_float32 is True but for testing result comparision make it true.
2)_blocks_two: no_of_blocks=2,other default
3)_blocks_ten: no_of_blocks=10,other default
4)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
5)_fakeghost_four: fakeghost=4 ,other default
'''
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
	
class TestNothing(unittest.TestCase):

	def test_nothing_operation_sparse_input_default_value(self):		
		print("\n test_nothing_operation_sparse_input_default_value...")		
		v_output = vc.nothing(input_svar,  make_float32=False)		
		d_output = input_svar			
		msgs = "test_nothing_operation_sparse_input_default_value"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	
		
	def test_nothing_operation_sparse_input_blocks_two(self):		
		print("\n test_nothing_operation_sparse_input_blocks_two...")		
		v_output = vc.nothing(input_svar,  no_of_blocks=2,make_float32=False)		
		d_output = input_svar						
		msgs = "test_nothing_operation_sparse_input_blocks_two"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_nothing_operation_sparse_input_blocks_ten(self):		
		print("\n test_nothing_operation_sparse_input_blocks_ten...")		
		v_output = vc.nothing(input_svar,  no_of_blocks=10,make_float32=False)		
		d_output = input_svar			
		msgs = "test_nothing_operation_sparse_input_blocks_ten"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_nothing_operation_sparse_input_fakeghost_one(self):		
		print("\n test_nothing_operation_sparse_input_fakeghost_one...")		
		v_output = vc.nothing(input_svar,  fakeghost=1,make_float32=False)		
		d_output = input_svar			
		msgs = "test_nothing_operation_sparse_input_fakeghost_one"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_nothing_operation_sparse_input_fakeghost_four(self):		
		print("\n test_nothing_operation_sparse_input_fakeghost_four...")		
		v_output = vc.nothing(input_svar, fakeghost=4,make_float32=False)		
		d_output = input_svar			
		msgs = "test_nothing_operation_sparse_input_fakeghost_four"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	#not necessary output will be always different depen on input array values..	
	# def test_nothing_operation_sparse_input_make_float32_true(self):		
		# print("\n test_nothing_operation_sparse_input_make_float32_true...")		
		# v_output = vc.nothing(input_svar,scalar=5)		
		# d_output = input_svar					
		# msgs = "test_nothing_operation_sparse_input_make_float32_true"
		# self.assertFalse((d_output==v_output).all(), msg=msgs)
	
#dense operation testing.........

	def test_nothing_operation_dense_input_default_value(self):		
		print("\n test_nothing_operation_dense_input_default_value...")		
		v_output = vc.nothing(input_dvar,  make_float32=False)		
		d_output = input_dvar			
		msgs = "test_nothing_operation_dense_input_default_value"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	
		
	def test_nothing_operation_dense_input_blocks_two(self):		
		print("\n test_nothing_operation_dense_input_blocks_two...")		
		v_output = vc.nothing(input_dvar,  no_of_blocks=2,make_float32=False)		
		d_output = input_dvar			
		msgs = "test_nothing_operation_dense_input_blocks_two"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_nothing_operation_dense_input_blocks_ten(self):		
		print("\n test_nothing_operation_dense_input_blocks_ten...")		
		v_output = vc.nothing(input_dvar,  no_of_blocks=10,make_float32=False)		
		d_output = input_dvar			
		msgs = "test_nothing_operation_dense_input_blocks_ten"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_nothing_operation_dense_input_fakeghost_one(self):		
		print("\n test_nothing_operation_dense_input_fakeghost_one...")		
		v_output = vc.nothing(input_dvar,  fakeghost=1,make_float32=False)		
		d_output = input_dvar			
		msgs = "test_nothing_operation_dense_input_fakeghost_one"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	def test_nothing_operation_dense_input_fakeghost_four(self):		
		print("\n test_nothing_operation_dense_input_fakeghost_four...")		
		v_output = vc.nothing(input_dvar, fakeghost=4,make_float32=False)		
		d_output = input_dvar						
		msgs = "test_nothing_operation_dense_input_fakeghost_four"
		self.assertTrue((d_output==v_output).all(), msg=msgs)
		
	#not necessary output will be always different depen on input array values..	
	# def test_nothing_operation_dense_input_make_float32_true(self):		
		# print("\n test_nothing_operation_dense_input_make_float32_true...")		
		# v_output = vc.nothing(input_dvar,scalar=5)		
		# d_output = input_svar						
		# msgs = "test_nothing_operation_dense_input_make_float32_true"
		# self.assertFalse((d_output==v_output).all(), msg=msgs)
		
if __name__ == '__main__':
    unittest.main()
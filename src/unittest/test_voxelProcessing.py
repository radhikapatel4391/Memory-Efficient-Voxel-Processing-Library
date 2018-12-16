import numpy as np
from scipy import sparse
from scipy import ndimage
import os
import time as t
import tempfile
import os,sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("voxelProcessing.py"))))
from voxelProcessing import VoxelProcessing

structure = ndimage.generate_binary_structure(3, 1)
operationArgumentDic = {"structure":structure,"iterations":1,"output":None,"origin":0,"mask":None, "border_value":0, "brute_force":False}

try:
	input_svar = np.load("sparse_array.npy", mmap_mode="r")
except:
	print("creating sparse input array will take time...")
	input_svar = random(400,160000,density=0.3,dtype="float64")
	input_svar = input_svar.todense()
	input_svar = np.array(input_svar)
	input_svar = np.reshape(input_svar,(400,400,400))
	np.save("sparse_array.npy", input_svar)
class VoxelTestCase(unittest.TestCase):
	def test_init(self):
		
		v = VoxelProcessing(input_svar,no_of_blocks=6,fakeghost=3,make_float32=False,operation="binary_dilation", operationArgumentDic = operationArgumentDic)
		self.assertEqual(v.get_X(),400,"wrong X size")
		self.assertEqual(v.get_Y(),400,"wrong Y size")
		self.assertEqual(v.get_Z(),400,"wrong Z size")
		self.assertEqual(v.get_make_float32(),False,"wrong get_make_float32")
		self.assertEqual(v.get_fakeghost(),3,"wrong get_fakeghost")
		self.assertEqual(v.get_sparsed(),True,"wrong get_sparsed")
		self.assertEqual(v.get_block_size(),80,"wrong get_block_size")
		self.assertEqual(v.get_no_of_blocks(),5,"wrong get_no_of_blocks")
		self.assertEqual(v.get_operation(),"binary_dilation","wrong get_operation")
		self.assertEqual(v.get_operationArgumentDic(),operationArgumentDic,"wrong get_operationArgumentDic")
		self.assertTrue(isinstance(v,VoxelProcessing), msg="not create instance of voxelprocessing")
		

	def test_main(self):
		v = VoxelProcessing(input_svar,no_of_blocks=6,fakeghost=3,make_float32=False,operation="binary_dilation", operationArgumentDic = operationArgumentDic)
		v_output = v.main()
		d_output = ndimage.binary_dilation(input_svar,structure=structure)				
		msgs = "binary_dilation_operation_FAIL_with parameters: "
		self.assertTrue((d_output==v_output).all(), msg=msgs)

if __name__ == '__main__':
    unittest.main()
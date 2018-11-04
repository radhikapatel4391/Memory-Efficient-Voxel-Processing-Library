import numpy as np
import os
from scipy import sparse
from scipy import ndimage

class VoxelProcessing:
    #npy file
    def __init__(self, filename,blockSize=50):        
        self.arr_map = np.load(filename, mmap_mode="r")
		self.x_dim = arr_map.shape[0]
        self.y_dim = arr_map.shape[1]
        self.z_dim = arr_map.shape[2]
		self.blockSize = blockSize
        
		
	def convert_to_2d(self):
        arr_2d = self.arr_map.reshape((self.arr_map.shape[0]*
                             self.arr_map.shape[1]), self.arr_map.shape[2])
        arr_2d = arr_2d.transpose()
        return arr_2d
		
	def compressed_storage(self, arr_2d):
        directory = 'compressed'
        output = 'output'
        CRS = sparse.csr_matrix(arr_2d, dtype='float32')
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(output):
            os.makedirs(output)
        sparse.save_npz("compressed/CRS.npz", CRS)
   
    '''Returns sparse matrix with Non-zero stored 
    elements in Compressed Sparse Row format'''
	def load_compressed(self):
        filename = "compressed/CRS.npz"
        try:
            CRS_RAM = open(filename, 'r')
        except:
            print('Cannot open', filename)
            return 0
        else:
            CRS_RAM = sparse.load_npz(filename)
            return CRS_RAM
            
    def get_no_of_blocks(self, arr_2d):
        arr_int = []
        for i in range(1, 11):
            block_size = arr_2d.shape[0] / i
            if float(block_size).is_integer():
                arr_int.append(i)
        block_size = arr_int[-1]
        print("No of blocks = ", block_size)
        print()
        return block_size
	
	
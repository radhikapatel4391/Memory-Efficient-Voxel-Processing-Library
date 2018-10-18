import numpy as np
import os
from scipy import sparse
from scipy import ndimage
from sys import getsizeof

class VoxelProcessing:
    
    def __init__(self, filename, dimension, structure):
        self.x_dim = dimension[0]
        self.y_dim = dimension[1]
        self.z_dim = dimension[2]
        self.struct_element = structure
        self.arr_map = np.memmap(filename, dtype=np.float64, 
                   mode='r', shape=(self.x_dim,self.y_dim,self.z_dim))
        
    def print_shape(self):
        print(self.arr_map.shape)
        
    def convert_to_2d(self):
        arr_2d = self.arr_map.reshape((self.arr_map.shape[0]*
                             self.arr_map.shape[1]), self.arr_map.shape[2])
        arr_2d = arr_2d.transpose()
        return arr_2d
    
    def compressed_storage(self, arr_2d):
        directory = 'compressed'
        CRS = sparse.csr_matrix(arr_2d)
        if not os.path.exists(directory):
            os.makedirs(directory)
        sparse.save_npz("compressed/CRS.npz", CRS)
   
    def load_compressed(self):
        filename = "compressed/CRS.npz"
        try:
            CRS_RAM = open(filename, 'r')
        except:
            print('Cannot open', filename)
            return 0
        else:
            CRS_RAM = sparse.load_npz(filename).todense()
            # os.remove(filename)
            # Returns a NumPy matrix object
            return CRS_RAM
            
    def get_no_of_blocks(self, arr_2d):
        arr_int = []
        for i in range(1, 11):
            block_size = arr_2d.shape[1] / i
            if float(block_size).is_integer():
                arr_int.append(i)
        block_size = arr_int[-1]
        print("No of blocks = ", block_size)
        print()
        return block_size

    def CRS_operation(self, CRS, n_blocks, operation):
        start_index = 0
        end_index = int(CRS.shape[1] / n_blocks)
        jump = int(CRS.shape[1] / n_blocks)
        for i in range(0, n_blocks):
            print("Start Index = ",start_index)
            print("End Index = ", end_index)
            block_2d = CRS[:,start_index:end_index]
            
            # Convert Numpy Matrix object to Numpy Array
            block_2d = np.squeeze(np.asarray(block_2d))
            print("Block_2d Memory size = ", getsizeof(block_2d))
            print("Block_2d Type = ", type(block_2d))
            block_2d = block_2d.T
            start_index = end_index
            end_index = end_index + jump
            self.convert_to_3d(i, block_2d, operation)
            
    def convert_to_3d(self, i, block_2d, operation):
        divide = [5, 10, 15, 20, 25]
        arr_int = []
        
        for k in range(0, len(divide)):
            value = block_2d.shape[0] / divide[k]
            if float(value).is_integer():
                arr_int.append(divide[k])
        n_splits = arr_int[-1]       
        
        #print(n_splits, block_2d.shape)
        mylist = np.split(block_2d, n_splits)
        block_3d = np.dstack(mylist)
        block_3d = np.rollaxis(block_3d,-1)
        print("Block_3d Memory size = ", getsizeof(block_3d))
        print("Block_3d Type = ", type(block_2d))
        if operation == 'dilation':
            print("Performing Dilation on blocks ", i)
            self.block_dilation(i, block_3d, self.struct_element)              
        if operation == 'erosion':
            print("Performing Erosion on block ", i)
            self.block_erosion(i, block_3d, self.struct_element)
    
    def block_dilation(self, i, block_3d, struct_element):
        dilated = ndimage.grey_dilation(block_3d, structure=struct_element)
        np.save("dilated_block" + str(i) + ".npy", dilated)
        print("Dilated_block size =",  getsizeof(dilated))
        print("Block Shape = ", dilated.shape)
        print()
        
    def block_erosion(self, i, block_3d, struct_element):
        eroded = ndimage.grey_erosion(block_3d, structure=struct_element)
        np.save("erosion_block" + str(i) + ".npy", eroded)
        print("Block Shape = ", eroded.shape)
        print()
from VoxelProcessing import VoxelProcessing
import numpy as np

if __name__ == '__main__':
    
    # Parameters
    # test = np.zeros((195,215,255))
    # np.save("test44.npy", test)
    filename = 'gyroidUniform.npy'
    dimension = [200, 200, 200]
    structure = np.zeros((3,3,3))
    operation = 'dilation'
    
    # Main
    data = VoxelProcessing(filename, dimension, structure)
    arr_2d = data.convert_to_2d()
    data.compressed_storage(arr_2d)
    CRS = data.load_compressed()
    no_of_blocks = data.get_no_of_blocks(arr_2d)
    data.CRS_operation(CRS, no_of_blocks, operation)
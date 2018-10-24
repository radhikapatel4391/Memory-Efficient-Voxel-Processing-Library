from VoxelProcessing import VoxelProcessing
import numpy as np

if __name__ == '__main__':
    
    # Parameters
    filename = 'gyroidUniform.npy'
    dimension = [200, 200, 200]
    a = np.random.uniform(size=(3,9))
    structure = a.reshape(3,3,3)
    operation = 'dilation'
    
    # Main
    data = VoxelProcessing(filename, dimension, structure)
    arr_2d = data.convert_to_2d()
    no_of_blocks = data.get_no_of_blocks(arr_2d)
    data.compressed_storage(arr_2d)    
    CRS = data.load_compressed()    
    data.Morphology(CRS, no_of_blocks, operation)
    data.merge_blocks()
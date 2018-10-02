import dask.array as da
import numpy as np
dirname = '../data/'
filename = dirname + 'gyroidUniform.npy'

# Map numpy to .npy file 
np_map = np.memmap(filename, dtype=np.float64, 
                   mode='r', shape=(200,200,200))

# Map Dask array to numpy array
dask_arr = da.from_array(np_map, chunks=(25))

# Split into Blocks
da.to_npy_stack(dirname, dask_arr, axis=0)

# Load Blocks
one = np.load(dirname +'0.npy')
two = np.load(dirname +'1.npy')
three = np.load(dirname +'2.npy')
four = np.load(dirname +'3.npy')
five = np.load(dirname +'4.npy')
six = np.load(dirname +'5.npy')
seven = np.load(dirname +'6.npy')
eight = np.load(dirname +'7.npy')

import dask.array as da
import numpy as np
dirname = '../data/'
filename = dirname + 'gyroidUniform.npy'

# Map numpy to file 
np_map = np.memmap(filename, dtype=np.float64, 
                   mode='r', shape=(200,200,200))

# Map Dask array to numpy array
dask_arr = da.from_array(np_map, chunks=(25))

# Split into Blocks
da.to_npy_stack(dirname, dask_arr, axis=0)

# Load Blocks
one = np.load('0.npy')
two = np.load('1.npy')
three = np.load('2.npy')
four = np.load('3.npy')
five = np.load('4.npy')
six = np.load('5.npy')
seven = np.load('6.npy')
eight = np.load('7.npy')

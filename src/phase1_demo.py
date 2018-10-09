from sys import getsizeof
from scipy import ndimage
import numpy as np
from scipy import sparse
dirname = '../data/'    

# Map numpy to file 
a = np.memmap('gyroidUniform.npy', dtype=np.float64, 
                   mode='r', shape=(200,200,200))

# Convert 3d array to 2d array
new_img = a.reshape((a.shape[0]*a.shape[1]), a.shape[2])
new_img = new_img.transpose()

# Compressed row Storage
CRS = sparse.csc_matrix(new_img)
sparse.save_npz("CRS.npz", CRS)
CRS_RAM = sparse.load_npz("CRS.npz")

# Extract 2d blocks from CRS
block_size = 25
index = block_size * a.shape[0]
block_2d = CRS_RAM[:,0:index].todense()
block_2d = block_2d.T

# Convert 2d blocks to 3d
mylist = np.split(block_2d, block_size)
block_3d = np.ma.dstack(mylist)
block_3d = np.rollaxis(block_3d,-1)

# Grey dilation
dilation = ndimage.grey_dilation(block_3d, structure=np.zeros((3,3,3)))
from sys import getsizeof
from scipy import ndimage
import numpy as np
from scipy import sparse
import sys
dirname = '../data/'    
def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size
# Map numpy to file 
a = np.memmap('../data/gyroidUniform/gyroidUniform.npy', dtype=np.float64, 
                   mode='r', shape=(200,200,200))

print("a mammap size,shape,type:      ",get_size(a),a.shape,a.dtype,type(a),sep="\t")
# Convert 3d array to 2d array
new_img = a.reshape((a.shape[0]*a.shape[1]), a.shape[2])
new_img = new_img.transpose()
print("new_img size,shape,type:       ",sys.getsizeof(new_img),new_img.shape,new_img.dtype,type(new_img),sep="\t")

# Compressed row Storage
CRS = sparse.csc_matrix(new_img)
print("CRS size,shape,type:            ",sys.getsizeof(CRS),CRS.shape,CRS.dtype,type(CRS),sep="\t")
sparse.save_npz("CRS.npz", CRS)
CRS_RAM = sparse.load_npz("CRS.npz")
print("CRS_RAM size,shape,type:        ",sys.getsizeof(CRS_RAM),CRS_RAM.shape,CRS_RAM.dtype,type(CRS_RAM),sep="\t")
# Extract 2d blocks from CRS
block_size = 25
index = block_size * a.shape[0]
print("index: ", index)
block_2d = CRS_RAM[:,0:index].toarray()
print("block_2d size,shape,type:       ",sys.getsizeof(block_2d),block_2d.shape,block_2d.dtype,type(block_2d),sep="\t")
block_2d = block_2d.T
print("final block_2d size,shape,type: ",sys.getsizeof(block_2d),block_2d.shape,block_2d.dtype,type(block_2d),sep="\t")

# Convert 2d blocks to 3d
mylist = np.split(block_2d, block_size)
block_3d = np.ma.dstack(mylist)
block_3d = np.rollaxis(block_3d,-1)
print("block_3d size,shape,type:       ",sys.getsizeof(block_3d),block_3d.shape,block_3d.dtype,type(block_3d),sep="\t")

# Grey dilation
dilation = ndimage.grey_dilation(block_3d, structure=np.zeros((3,3,3)))
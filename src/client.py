import voxel as vc
from scipy.sparse import random
import time as t
import numpy as np
from scipy import ndimage
import os


structure = np.ones((3,3,3))
#.............test1. dense.......
filename = 'gyroidUniform.npy'   		
input = np.load(filename, mmap_mode="r")



print("..............................dense..............................................")
#Nothing..............
print("\n nothing testing...")
output = vc.nothing(input,blockSize=50,fakeGhost=4)

#print("\nresult: ",(input==output).all())
#......................................

#grey_dilation..............
print("\ngrey_dilation VoxelProcessind")
output = vc.grey_dilation(input,structure=structure)
print("\ngrey_dilation Default")
d = ndimage.grey_dilation(input,structure=structure)

#print("\nresult: ",(d==output).all())
#......................................

print("..............................Sparse..............................................")
#Sparse.....................................................Sparse.......................
input = random(500,560000,density=0.3,dtype="float64")
input = input.todense()
input = np.array(input)
input = np.reshape(input,(500,700,800))

#Nothing..................
print("\n sparse_nothing testing...")
output = vc.nothing(input,blockSize=50,fakeGhost=4)
#print("\nresult: ",(input==output).all())

#grey_dilation..............
print("\ngrey_dilation VoxelProcessind")
output = vc.grey_dilation(input,structure=structure)
print("\ngrey_dilation Default")
d = ndimage.grey_dilation(input,structure=structure)
#print("\nresult: ",(d==output).all())
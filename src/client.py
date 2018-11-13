import voxel as vc
from scipy.sparse import random
import time as t
import numpy as np
from scipy import ndimage
import os
import psutil

structure = np.ones((3,3,3))
#generating sparse array of different size...
input = random(40000,200,density=0.5,dtype="float64")
input = input.todense()
input = np.array(input)
input = np.reshape(input,(200,200,200))
#............



#...............

print("\nNothing testing....")
output = vc.nothing(input,fakeGhost=3)
print("result: ",(input==output).all())



#.......test1.sparse.........
print("\ngrey_dilation VoxelProcessind")
output = vc.grey_dilation(input,fakeGhost=3,structure=structure)
#......
print("\ngrey_dilation Default")
d = ndimage.grey_dilation(input,structure=structure)
print("\nresult: ",(d==output).all())


#.............test2. dense.......
filename = 'gyroidUniform.npy'   		
input = np.load(filename, mmap_mode="r")

#..............
print("\ngrey_dilation VoxelProcessind")
output = vc.grey_dilation(input,fakeGhost=3,structure=structure)
# #......
print("\ngrey_dilation Default")
d = ndimage.grey_dilation(input,structure=structure)

print("\nresult: ",(d==output).all())

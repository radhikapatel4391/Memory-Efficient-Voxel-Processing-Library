import voxel as vc
from scipy.sparse import random
import time as t
import numpy as np
from scipy import ndimage
import os
import psutil

# print(psutil.cpu_percent())
# print(psutil.virtual_memory())
process = psutil.Process(os.getpid())
#print("client PID: ",psutil.Process(os.getpid()))
print(process.memory_info())

filename = 'gyroidUniform.npy'   
structure = np.ones((3,3,3))

#generating sparse array of different size...
input = random(40000,200,density=0.5,dtype="float64")
input = input.todense()
input = np.array(input)
input = np.reshape(input,(200,200,200))
#............



#...............
print(process.memory_info())
print("\nNothing testing....")
start_time = t.time()
x = int(process.memory_info().rss)
output = vc.nothing(input,fakeGhost=3)
y = int(process.memory_info().rss)
print("Memory: ",(y-x)/1000000)
print("sec:    ",(t.time() - start_time))
print("result: ",(input==output).all())


print(process.memory_info())
#.......test1..........
print("\ngrey_dilation VoxelProcessind")
start_time = t.time()
x = int(process.memory_info().rss)
output = vc.grey_dilation(input,fakeGhost=3,structure=structure)
y = int(process.memory_info().rss)
print("Memory: ",(y-x)/1000000)
print("sec:    ",(t.time() - start_time))
# python -m memory_profiler memory.py
print(process.memory_info())
#......
print("\ngrey_dilation Default")
start_time = t.time()
x = int(process.memory_info().rss)
d = ndimage.grey_dilation(input,structure=structure)
y = int(process.memory_info().rss)
print("Memory: ",(y-x)/1000000)
print("sec:    ",(t.time() - start_time))
print(process.memory_info())

print("\nresult: ",(d==output).all())

print(process.memory_info())
#.............test2........		
input = np.load(filename, mmap_mode="r")
print(process.memory_info())
#..............
print("\ngrey_dilation VoxelProcessind")
start_time = t.time()
x = int(process.memory_info().rss)
output = vc.grey_dilation(input,fakeGhost=3,structure=structure)
y = int(process.memory_info().rss)
print("Memory: ",(y-x)/1000000)
print("sec:    ",(t.time() - start_time))

print(process.memory_info())
# #......
print("\ngrey_dilation Default")
start_time = t.time()
x = int(process.memory_info().rss)
d = ndimage.grey_dilation(input,structure=structure)
y = int(process.memory_info().rss)
print("Memory: ",(y-x)/1000000)
print("sec:    ",(t.time() - start_time))

print("\nresult: ",(d==output).all())
print(process.memory_info().rss)
print(process.memory_info())
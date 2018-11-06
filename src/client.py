import voxel as vc
from scipy.sparse import random
import time as t
import numpy as np
from scipy import ndimage
import os
import psutil
process = psutil.Process(os.getpid())
print("client PID: ",psutil.Process(os.getpid()))
#print(process.memory_info().rss)

filename = 'gyroidUniform.npy'   
structure = np.ones((3,3,3))
#input = np.load(filename, mmap_mode="r")
#print(process.memory_info().rss)

#generating sparse array of different size...
input = random(40000,200,density=0.5,dtype="float64")
input = input.todense()
input = np.array(input)
input = np.reshape(input,(200,200,200))
#............

#Test start...............

#...............
print("Nothing testing....")
start_time = t.time()
process = psutil.Process(os.getpid())
x = int(process.memory_info().rss)
output = vc.nothing(input)
y = int(process.memory_info().rss)
print("------------momory used: ",y-x)
print("VC--- %s seconds ---" % (t.time() - start_time))
print("result: ",(input==output).all())



#..............
print("grey_dilation testing...")
start_time = t.time()
process = psutil.Process(os.getpid())
x = int(process.memory_info().rss)
output = vc.grey_dilation(input,structure=structure)
y = int(process.memory_info().rss)
print("----------------momory used: ",y-x)
print("VC--- %s seconds ---" % (t.time() - start_time))
#......
start_time = t.time()
process = psutil.Process(os.getpid())
x = int(process.memory_info().rss)
d = ndimage.grey_dilation(input,structure=structure)
y = int(process.memory_info().rss)
print("----------------momory used: ",y-x)
print("DE--- %s seconds ---" % (t.time() - start_time))
print("result: ",(d==output).all())

#.....................		
	
import voxel as vc
from scipy.sparse import random
import time as t
import numpy as np
from scipy import ndimage
import os
import psutil

#pip install -U memory_profiler
# input = random(160000,4000,density=0.5,dtype="float64")
# input = input.todense()
# input = np.array(input)
# input = np.reshape(input,(400,400,4000))
# print(input.shape,input.dtype,input.size,input.nbytes)
@profile
def main():
	filename = 'gyroidUniform.npy'	
	input = np.load(filename, mmap_mode="r")
	structure = np.ones((3,3,3))	
	#output = vc.grey_dilation(input,structure=structure)
	output = ndimage.grey_dilation(input,structure=structure)

if __name__ == '__main__':
	main()
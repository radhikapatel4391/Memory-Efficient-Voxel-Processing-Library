import numpy as np
import os
from scipy import sparse
from scipy import ndimage
def grey_dilation(input,blockSize=20, size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	x = input.shape[0]
	y = input.shape[1]
	z = input.shape[2]
	input = input.reshape(x,y*z)    
	while(z % blockSize!=0):
		blockSize -= 1
	n_blocks = z // blockSize
	input = sparse.csr_matrix(input)        
    sparse.save_npz("CRS.npz", input)
	start_index = 0
    fake_ghost = 1
	jump = y*blockSize
	end_index = jump + y*fake_ghost
	if end_index > input.shape[1]:
		end_index = input.shape[1]
	f_handle = open('output/binary', 'wb')
	for i in range(0, n_blocks):
		print("Start Index = ",start_index)
		print("End Index = ", end_index)
		block_2d = input[:,start_index:end_index].toarray()
		mylist = np.split(block_2d, blockSize)
		block_3d = np.dstack(mylist)
		dilated = ndimage.grey_dilation(dilated, structure=structure)
		print("dilated image shape: "dilated.shape)
		if i == 0:
			dilated = dilated[0:end_index-(y*fake_ghost),:,:]
		elif i == n_blocks - 1:
			dilated = dilated[start_index-y*fake_ghost:x,:,:]
		else:
			dilated = dilated[start_index-y*fake_ghost:end_index-(y*fake_ghost),:,:]
		dilated.tofile(f_handle)
		start_index = end_index - 2*y*fake_ghost
		end_index = end_index = jump + y*fake_ghost
		if end_index > input.shape[1]:
			end_index = input.shape[1]
    f_handle.close()
	merging = np.memmap("output/binary",mode='r', shape=(self.x_dim,self.y_dim,self.z_dim))
	np.save("output.npy", merging)
	
filename = 'gyroidUniform.npy'   
structure = np.ones((3,3,3))
input = np.load(filename, mmap_mode="r")
grey_dilation(input,structure=structure)
	
	
	
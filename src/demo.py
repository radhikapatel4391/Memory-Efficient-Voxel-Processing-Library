import voxel as vc
import numpy as np
from scipy.sparse import random

'''
demo of how to call each method of voxel module.

1 binary_dilation()
2 binary_erosion()
3 binary_closing()
4 binary_opening()
5 binary_hit_or_miss()
6 binary_propagation()
7 binary_fill_holes()
8 black_tophat()
9 grey_dilation()
10 grey_erosion()
11 grey_closing()
12 grey_opening()
13 morphological_gradient()
14 morphological_laplace()
15 white_tophat()
16 multiply() (integer/float valut multiplication with each element.)
17 nothing() (not perform any operation just do blocking and merging.)

'''

# try:
	# input_dvar = np.load("dense_array.npy", mmap_mode="r")
# except:	
	# print("creating dense input array will take time...")
	# structure = np.ones((3,3,3))
	# input_dvar = random(400,160000,density=0.7,dtype="float64")
	# input_dvar = input_dvar.todense()
	# input_dvar = np.array(input_dvar)
	# input_dvar = np.reshape(input_dvar,(400,400,400))
	# np.save("dense_array.npy", input_dvar)

# creating sparse input array
structure = np.ones((3,3,3))
try:
	input_svar = np.load("sparse_array.npy", mmap_mode="r")
except:
	print("creating sparse input array will take time...")
	input_svar = random(400,160000,density=0.3,dtype="float64")
	input_svar = input_svar.todense()
	input_svar = np.array(input_svar)
	input_svar = np.reshape(input_svar,(400,400,400))
	np.save("sparse_array.npy", input_svar)

input_var = input_svar #input_dvar

#1.
output_var = vc.binary_dilation(input_var,no_of_blocks=4,fakeghost=2,make_float32=True, structure = structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
#2	
output_var = vc.binary_erosion(input_var,no_of_blocks=4,fakeghost=2,make_float32=True, structure = structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
#3	
output_var = vc.binary_closing(input_var,no_of_blocks=4,fakeghost=2,make_float32=True, structure = structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)	
#4	
output_var = vc.binary_opening(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  structure = structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
#5
output_var = vc.binary_fill_holes(input_var,no_of_blocks=4,fakeghost=2,make_float32=True, structure = structure, output=None, origin=0)
#6	
output_var = vc.binary_hit_or_miss(input_var, no_of_blocks=4,fakeghost=2,make_float32=True, structure1=None, structure2=None, output=None, origin1=0, origin2=None)
#7
output_var = vc.binary_propagation(input_var,no_of_blocks=4,fakeghost=2,make_float32=True, structure = structure, mask=None, output=None, border_value=0, origin=0)
#8	
output_var = vc.black_tophat(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure = structure, output=None, mode='reflect', cval=0.0, origin=0)
#9
output_var = vc.grey_dilation(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,size=None, footprint=None, structure = structure, output=None, mode='reflect', cval=0.0, origin=0)
#10	
output_var = vc.grey_erosion(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure = structure, output=None, mode='reflect', cval=0.0, origin=0)
#11	
output_var = vc.grey_closing(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure = structure, output=None, mode='reflect', cval=0.0, origin=0)
#12	
output_var = vc.grey_opening(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure = structure, output=None, mode='reflect', cval=0.0, origin=0)
#13	
output_var = vc.morphological_gradient(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure = structure, output=None, mode='reflect', cval=0.0, origin=0)
#14	
output_var = vc.morphological_laplace(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure = structure, output=None, mode='reflect', cval=0.0, origin=0)
#15	
output_var = vc.white_tophat(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure = structure, output=None, mode='reflect', cval=0.0, origin=0)
#16	
output_var = vc.multiply(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,scalar=1)
#17
output_var = vc.nothing(input_var,no_of_blocks=4,fakeghost=2,make_float32=True)
	
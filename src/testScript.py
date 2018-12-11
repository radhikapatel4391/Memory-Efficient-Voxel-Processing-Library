import voxel as vc
from scipy.sparse import random
import time as t
import numpy as np
from scipy import ndimage
import os
'''
test script which perform all  morphological operation to check all operation provided by module working as expected or not.
On console print true if output is as expected(same as default scipy module.)
Along with that it print time taken by default scipy module and using our approach.
To test dense method generate dense array with 0.3 desity.

'''
# creating input array
print("creating input array will take time...")
structure = np.ones((3,3,3))
input_var = random(400,160000,density=0.7,dtype="float64")
input_var = input_var.todense()
input_var = np.array(input_var)
input_var = np.reshape(input_var,(400,400,400))



print("..............................dense operation testing..............................................")

#0.Nothing..............
print("\n nothing testing...")
start_time = t.time()
output = vc.nothing(input_var,no_of_blocks=7,fakeghost=4,make_float32=False)
print("nothing: ",(t.time() - start_time))
print("\nresult: ",(input_var==output).all())
print(output.dtype,input_var.dtype)
#1.grey_dilation..............
print("\ngrey_dilation VoxelProcessind")
start_time = t.time()
output = vc.grey_dilation(input_var,no_of_blocks=6,structure=structure,make_float32=False)
print("grey_dilation: ",(t.time() - start_time))
print("\ngrey_dilation Default")
start_time = t.time()
d = ndimage.grey_dilation(input_var,structure=structure)
print("default grey_dilation: ",(t.time() - start_time))
print("\nresult: ",(d==output).all())
print(output.dtype,input_var.dtype)
#2.grey_erosion..............
print("\ngrey_erosion VoxelProcessind")
output = vc.grey_erosion(input_var,no_of_blocks=7, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\ngrey_erosion Default")
d = ndimage.grey_erosion(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\nresult: ",(d==output).all())
#3.grey_closing..............
print("\ngrey_closing VoxelProcessind")
output = vc.grey_closing(input_var,make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\ngrey_closing Default")
d = ndimage.grey_closing(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\nresult: ",(d==output).all())
print(output.dtype,input_var.dtype)
#4.grey_opening..............
print("\ngrey_opening VoxelProcessind")
output = vc.grey_opening(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\ngrey_opening Default")
d = ndimage.grey_opening(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\nresult: ",(d==output).all())
#5.binary_closing..............
print("\nbinary_closing VoxelProcessind")
output = vc.binary_closing(input_var,make_float32=False,structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("\nbinary_closing Default")
d = ndimage.binary_closing(input_var,structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("\nresult: ",(d==output).all())
print(output[151][151][151])
#6.binary_opening..............
print("\nbinary_opening VoxelProcessind")
output = vc.binary_opening(input_var, structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("\nbinary_opening Default")
d = ndimage.binary_opening(input_var, structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("\nresult: ",(d==output).all())
#7.binary_dilation..............
print("\nbinary_dilation VoxelProcessind")
output = vc.binary_dilation(input_var,make_float32=False,  structure=structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("\nbinary_dilation Default")
d = ndimage.binary_dilation(input_var, structure=structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("\nresult: ",(d==output).all())
#8.binary_erosion..............
print("\nbinary_erosion VoxelProcessind")
output = vc.binary_erosion(input_var, make_float32=False,  structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("\nbinary_erosion Default")
d = ndimage.binary_erosion(input_var, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("\nresult: ",(d==output).all())
#9.binary_fill_holes..............
print("\nbinary_fill_holes VoxelProcessind")
output = vc.binary_fill_holes(input_var, make_float32=False,  structure=None, output=None, origin=0)
print("\nbinary_fill_holes Default")
d = ndimage.binary_fill_holes(input_var, structure=None, output=None, origin=0)
print("\nresult: ",(d==output).all())
#10.binary_hit_or_miss..............
print("\nbinary_hit_or_miss VoxelProcessind")
output = vc.binary_hit_or_miss(input_var, make_float32=False,  structure1=None, structure2=None, output=None, origin1=0, origin2=None)
print("\nbinary_hit_or_miss Default")
d = ndimage.binary_hit_or_miss(input_var, structure1=None, structure2=None, output=None, origin1=0, origin2=None)
print("\nresult: ",(d==output).all())
#11.binary_propagation..............
print("\nbinary_propagation VoxelProcessind")
output = vc.binary_propagation(input_var, make_float32=False,  structure=None, mask=None, output=None, border_value=0, origin=0)
print("\nbinary_propagation Default")
d = ndimage.binary_propagation(input_var, structure=None, mask=None, output=None, border_value=0, origin=0)
print("\nresult: ",(d==output).all())
#12.black_tophat..............
print("\nblack_tophat VoxelProcessind")
output = vc.black_tophat(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\nblack_tophat Default")
d = ndimage.black_tophat(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\nresult: ",(d==output).all())
#13.morphological_gradient..............
print("\nmorphological_gradient VoxelProcessind")
output = vc.morphological_gradient(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\nmorphological_gradient Default")
d = ndimage.morphological_gradient(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\nresult: ",(d==output).all())
#14.morphological_laplace..............
print("\nmorphological_laplace VoxelProcessind")
output = vc.morphological_laplace(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\nmorphological_laplace Default")
d = ndimage.morphological_laplace(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\nresult: ",(d==output).all())
#15.white_tophat..............
print("\nwhite_tophat VoxelProcessind")
output = vc.white_tophat(input_var, make_float32=False, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\nwhite_tophat VoxelProcessind Default")
d = ndimage.white_tophat(input_var,size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("\nresult: ",(d==output).all())
#16.intMultiply..............
print("\nintMultiply VoxelProcessind")
output = vc.intMultiply(input_var, make_float32=False, no_of_blocks=7,fakeghost=1,scalar=10)
print("\nintMultiply Default")
d = input_var*10
print("\nresult: ",(d==output).all())





print("\n\ncreating input array will take time...")
input_var = random(400,160000,density=0.3,dtype="float64")
input_var = input_var.todense()
input_var = np.array(input_var)
input_var = np.reshape(input_var,(400,400,400))
#input_var = np.load("400_400_400_0.3.npy", mmap_mode="r")

print("..............................Sparse operation testing..............................................")
#0.Nothing..............
print("\n nothing testing...")
start_time = t.time()
output = vc.nothing(input_var,no_of_blocks=7,fakeghost=4,make_float32=False)
print("nothing: ",(t.time() - start_time))
print("\nresult: ",(input_var==output).all())
print(output.dtype,input_var.dtype)
#1.grey_dilation..............
print("\ngrey_dilation VoxelProcessind")
start_time = t.time()
output = vc.grey_dilation(input_var,no_of_blocks=6,structure=structure,make_float32=False)
print("grey_dilation: ",(t.time() - start_time))
print("\ngrey_dilation Default")
start_time = t.time()
d = ndimage.grey_dilation(input_var,structure=structure)
print("default grey_dilation: ",(t.time() - start_time))
print("\nresult: ",(d==output).all())
print(output.dtype,input_var.dtype)
#2.grey_erosion..............
print("\ngrey_erosion VoxelProcessind")
output = vc.grey_erosion(input_var, make_float32=False,structure=structure)
print("\ngrey_erosion Default")
d = ndimage.grey_erosion(input_var,structure=structure)
print("\nresult: ",(d==output).all())
#3.grey_closing..............
print("\ngrey_closing VoxelProcessind")
output = vc.grey_closing(input_var,make_float32=False,  structure=structure)
print("\ngrey_closing Default")
d = ndimage.grey_closing(input_var,structure=structure)
print("\nresult: ",(d==output).all())
print(output.dtype,input_var.dtype)
#4.grey_opening..............
print("\ngrey_opening VoxelProcessind")
output = vc.grey_opening(input_var, make_float32=False,structure=structure)
print("\ngrey_opening Default")
d = ndimage.grey_opening(input_var,structure=structure)
print("\nresult: ",(d==output).all())
#5.binary_closing..............
print("\nbinary_closing VoxelProcessind")
output = vc.binary_closing(input_var,make_float32=False)
print("\nbinary_closing Default")
d = ndimage.binary_closing(input_var)
print("\nresult: ",(d==output).all())
#6.binary_opening..............
print("\nbinary_opening VoxelProcessind")
output = vc.binary_opening(input_var,make_float32=False)
print("\nbinary_opening Default")
d = ndimage.binary_opening(input_var)
print("\nresult: ",(d==output).all())
#7.binary_dilation..............
print("\nbinary_dilation VoxelProcessind")
output = vc.binary_dilation(input_var,make_float32=False, structure=structure)
print("\nbinary_dilation Default")
d = ndimage.binary_dilation(input_var, structure=structure)
print("\nresult: ",(d==output).all())
#8.binary_erosion..............
print("\nbinary_erosion VoxelProcessind")
output = vc.binary_erosion(input_var, make_float32=False)
print("\nbinary_erosion Default")
d = ndimage.binary_erosion(input_var)
print("\nresult: ",(d==output).all())
#9.binary_fill_holes..............
print("\nbinary_fill_holes VoxelProcessind")
output = vc.binary_fill_holes(input_var, make_float32=False)
print("\nbinary_fill_holes Default")
d = ndimage.binary_fill_holes(input_var)
print("\nresult: ",(d==output).all())
#10.binary_hit_or_miss..............
print("\nbinary_hit_or_miss VoxelProcessind")
output = vc.binary_hit_or_miss(input_var,make_float32=False)
print("\nbinary_hit_or_miss Default")
d = ndimage.binary_hit_or_miss(input_var)
print("\nresult: ",(d==output).all())
#11.binary_propagation..............
print("\nbinary_propagation VoxelProcessind")
output = vc.binary_propagation(input_var, make_float32=False)
print("\nbinary_propagation Default")
d = ndimage.binary_propagation(input_var)
print("\nresult: ",(d==output).all())
#12.black_tophat..............
print("\nblack_tophat VoxelProcessind")
output = vc.black_tophat(input_var,make_float32=False,structure=structure)
print("\nblack_tophat Default")
d = ndimage.black_tophat(input_var,structure=structure)
print("\nresult: ",(d==output).all())
#13.morphological_gradient..............
print("\nmorphological_gradient VoxelProcessind")
output = vc.morphological_gradient(input_var, structure=structure,make_float32=False,)
print("\nmorphological_gradient Default")
d = ndimage.morphological_gradient(input_var,structure=structure)
print("\nresult: ",(d==output).all())
#14.morphological_laplace..............
print("\nmorphological_laplace VoxelProcessind")
output = vc.morphological_laplace(input_var,structure=structure,make_float32=False)
print("\nmorphological_laplace Default")
d = ndimage.morphological_laplace(input_var,structure=structure)
print("\nresult: ",(d==output).all())
#15.white_tophat..............
print("\nwhite_tophat VoxelProcessind")
output = vc.white_tophat(input_var, make_float32=False,structure=structure)
print("\nwhite_tophat VoxelProcessind Default")
d = ndimage.white_tophat(input_var,structure=structure)
print("\nresult: ",(d==output).all())
#16.intMultiply..............
print("\nintMultiply VoxelProcessind")
output = vc.intMultiply(input_var, make_float32=False,scalar=10)
print("\nintMultiply Default")
d = input_var*10
print("\nresult: ",(d==output).all())

# print(output[134][156][98])
# print(d[134][156][98])
# t = np.setdiff1d(output, d)
# print(len(t))
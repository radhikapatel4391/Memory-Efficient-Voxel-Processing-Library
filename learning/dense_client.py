import voxel as vc
from scipy.sparse import random
import time as t
import numpy as np
from scipy import ndimage
import os
import unittest

'''with out unit testing usage demo.. 
output = vc.grey_dilation(input_var,structure=structure,no_of_blocks=6,fakeghost=4,make_float32=False)

'''

print("creating dense input array will take time...")
structure = np.ones((3,3,3))
# input_var = random(400,160000,density=0.7,dtype="float64")
# input_var = input_var.todense()
# input_var = np.array(input_var)
# input_var = np.reshape(input_var,(400,400,400))
#np.save("400_.7_dense", input_var)
input_var = np.load("400_.7_dense.npy", mmap_mode="r")
print("..............................dense operation testing..............................................")
#5.binary_closing..............
print("\nbinary_closing VoxelProcessing")
start_time = t.time()
output = vc.binary_closing(input_var,make_float32=False,no_of_blocks=4,fakeghost=2,structure=structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("vc binary_closing: ",(t.time() - start_time)," sec")
print("\nbinary_closing Default")
start_time = t.time()
d = ndimage.binary_closing(input_var,structure=structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("scipy binary_closing: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#6.binary_opening..............
print("\nbinary_opening VoxelProcessing")
start_time = t.time()
output = vc.binary_opening(input_var, make_float32=False,no_of_blocks=4,fakeghost=2,structure=structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("vc binary_opening: ",(t.time() - start_time)," sec")
print("\nbinary_opening Default")
start_time = t.time()
d = ndimage.binary_opening(input_var, structure=structure, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
print("scipy binary_opening: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#9.binary_fill_holes..............
print("\nbinary_fill_holes VoxelProcessing")
start_time = t.time()
output = vc.binary_fill_holes(input_var, make_float32=False,structure=structure)
print("vc binary_fill_holes: ",(t.time() - start_time)," sec")
print("\nbinary_fill_holes Default")
start_time = t.time()
d = ndimage.binary_fill_holes(input_var, structure=structure)
print("scipy binary_fill_holes: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#0.Nothing..............
print("\n nothing testing...")
start_time = t.time()
output = vc.nothing(input_var,no_of_blocks=7,fakeghost=4,make_float32=False)
print("vc nothing: ",(t.time() - start_time)," sec")
print("\nresult: ",(input_var==output).all())

#1.grey_dilation..............
print("\ngrey_dilation VoxelProcessing")
start_time = t.time()
output = vc.grey_dilation(input_var,no_of_blocks=6,structure=structure,make_float32=False)
print("vc grey_dilation: ",(t.time() - start_time)," sec")
print("\ngrey_dilation Default")
start_time = t.time()
d = ndimage.grey_dilation(input_var,structure=structure)
print("scipy grey_dilation: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#2.grey_erosion..............
print("\ngrey_erosion VoxelProcessing")
start_time = t.time()
output = vc.grey_erosion(input_var,no_of_blocks=7, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc grey_erosion: ",(t.time() - start_time)," sec")
print("\ngrey_erosion Default")
start_time = t.time()
d = ndimage.grey_erosion(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy grey_erosion: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#3.grey_closing..............
print("\ngrey_closing VoxelProcessing")
start_time = t.time()
output = vc.grey_closing(input_var,make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc grey_closing: ",(t.time() - start_time)," sec")
print("\ngrey_closing Default")
start_time = t.time()
d = ndimage.grey_closing(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy grey_closing: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#4.grey_opening..............
print("\ngrey_opening VoxelProcessing")
start_time = t.time()
output = vc.grey_opening(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc grey_opening: ",(t.time() - start_time)," sec")
print("\ngrey_opening Default")
start_time = t.time()
d = ndimage.grey_opening(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy grey_opening: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#7.binary_dilation..............
print("\nbinary_dilation VoxelProcessing")
start_time = t.time()
output = vc.binary_dilation(input_var,make_float32=False,  structure=structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("vc binary_dilation: ",(t.time() - start_time)," sec")
print("\nbinary_dilation Default")
start_time = t.time()
d = ndimage.binary_dilation(input_var, structure=structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("scipy binary_dilation: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#8.binary_erosion..............
print("\nbinary_erosion VoxelProcessing")
start_time = t.time()
output = vc.binary_erosion(input_var, make_float32=False,structure=structure,iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("vc binary_erosion: ",(t.time() - start_time)," sec")
print("\nbinary_erosion Default")
start_time = t.time()
d = ndimage.binary_erosion(input_var, structure=structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
print("scipy binary_erosion: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())

#10.binary_hit_or_miss..............
print("\nbinary_hit_or_miss VoxelProcessing")
start_time = t.time()
output = vc.binary_hit_or_miss(input_var, make_float32=False,  structure1=structure, structure2=None, output=None, origin1=0, origin2=None)
print("vc binary_hit_or_miss: ",(t.time() - start_time)," sec")
print("\nbinary_hit_or_miss Default")
start_time = t.time()
d = ndimage.binary_hit_or_miss(input_var, structure1=structure, structure2=None, output=None, origin1=0, origin2=None)
print("scipy binary_hit_or_miss: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#11.binary_propagation..............
print("\nbinary_propagation VoxelProcessing")
start_time = t.time()
output = vc.binary_propagation(input_var, make_float32=False,  structure=structure, mask=None, output=None, border_value=0, origin=0)
print("vc binary_propagation: ",(t.time() - start_time)," sec")
print("\nbinary_propagation Default")
start_time = t.time()
d = ndimage.binary_propagation(input_var, structure=structure, mask=None, output=None, border_value=0, origin=0)
print("scipy binary_propagation: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#12.black_tophat..............
print("\nblack_tophat VoxelProcessing")
start_time = t.time()
output = vc.black_tophat(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc black_tophat: ",(t.time() - start_time)," sec")
print("\nblack_tophat Default")
start_time = t.time()
d = ndimage.black_tophat(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy black_tophat: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#13.morphological_gradient..............
print("\nmorphological_gradient VoxelProcessing")
start_time = t.time()
output = vc.morphological_gradient(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc morphological_gradient: ",(t.time() - start_time)," sec")
print("\nmorphological_gradient Default")
start_time = t.time()
d = ndimage.morphological_gradient(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy morphological_gradient: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#14.morphological_laplace..............
print("\nmorphological_laplace VoxelProcessing")
start_time = t.time()
output = vc.morphological_laplace(input_var, make_float32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc morphological_laplace: ",(t.time() - start_time)," sec")
print("\nmorphological_laplace Default")
start_time = t.time()
d = ndimage.morphological_laplace(input_var, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy morphological_laplace: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#15.white_tophat..............
print("\nwhite_tophat VoxelProcessing")
start_time = t.time()
output = vc.white_tophat(input_var, make_float32=False, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("vc white_tophat: ",(t.time() - start_time)," sec")
print("\nwhite_tophat VoxelProcessing Default")
start_time = t.time()
d = ndimage.white_tophat(input_var,size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
print("scipy white_tophat: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())
#16.multiply..............
print("\nmultiply VoxelProcessing")
start_time = t.time()
output = vc.multiply(input_var, make_float32=False, no_of_blocks=7,fakeghost=2,scalar=10)
print("vc multiply: ",(t.time() - start_time)," sec")
print("\nmultiply Default")
start_time = t.time()
d = input_var*10
print("scipy multiply: ",(t.time() - start_time)," sec")
print("\nresult: ",(d==output).all())





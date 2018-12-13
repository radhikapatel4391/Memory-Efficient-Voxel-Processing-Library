import voxel as vc
from scipy.sparse import random
import numpy as np
from scipy import ndimage



def main():
	structure = np.ones((3,3,3))
	#.............test1. dense.......
	filename = 'gyroidUniform.npy'   		
	input = np.load(filename, mmap_mode="r")



	print("..............................dense..............................................")

	#0.Nothing..............
	print("\n nothing testing...")
	output = vc.nothing(input,blockSize=50,fakeGhost=4,makeFloat32=False)
	print("\nresult: ",(input==output).all())
	print(output.dtype,input.dtype)
	#1.grey_dilation..............
	print("\ngrey_dilation VoxelProcessind")
	output = vc.grey_dilation(input,structure=structure,makeFloat32=False)
	print("\ngrey_dilation Default")
	d = ndimage.grey_dilation(input,structure=structure)
	print("\nresult: ",(d==output).all())
	print(output.dtype,input.dtype)
	#2.grey_erosion..............
	print("\ngrey_erosion VoxelProcessind")
	output = vc.grey_erosion(input, makeFloat32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\ngrey_erosion Default")
	d = ndimage.grey_erosion(input, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\nresult: ",(d==output).all())
	#3.grey_closing..............
	print("\ngrey_closing VoxelProcessind")
	output = vc.grey_closing(input,makeFloat32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\ngrey_closing Default")
	d = ndimage.grey_closing(input, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\nresult: ",(d==output).all())
	print(output.dtype,input.dtype)
	#4.grey_opening..............
	print("\ngrey_opening VoxelProcessind")
	output = vc.grey_opening(input, makeFloat32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\ngrey_opening Default")
	d = ndimage.grey_opening(input, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\nresult: ",(d==output).all())
	#5.binary_closing..............
	print("\nbinary_closing VoxelProcessind")
	output = vc.binary_closing(input,makeFloat32=False,structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
	print("\nbinary_closing Default")
	d = ndimage.binary_closing(input,structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
	print("\nresult: ",(d==output).all())
	print(output[151][151][151])
	#6.binary_opening..............
	print("\nbinary_opening VoxelProcessind")
	output = vc.binary_opening(input, structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
	print("\nbinary_opening Default")
	d = ndimage.binary_opening(input, structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False)
	print("\nresult: ",(d==output).all())
	#7.binary_dilation..............
	print("\nbinary_dilation VoxelProcessind")
	output = vc.binary_dilation(input,makeFloat32=False,  structure=structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
	print("\nbinary_dilation Default")
	d = ndimage.binary_dilation(input, structure=structure, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
	print("\nresult: ",(d==output).all())
	#8.binary_erosion..............
	print("\nbinary_erosion VoxelProcessind")
	output = vc.binary_erosion(input, makeFloat32=False,  structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
	print("\nbinary_erosion Default")
	d = ndimage.binary_erosion(input, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)
	print("\nresult: ",(d==output).all())
	#9.binary_fill_holes..............
	print("\nbinary_fill_holes VoxelProcessind")
	output = vc.binary_fill_holes(input, makeFloat32=False,  structure=None, output=None, origin=0)
	print("\nbinary_fill_holes Default")
	d = ndimage.binary_fill_holes(input, structure=None, output=None, origin=0)
	print("\nresult: ",(d==output).all())
	#10.binary_hit_or_miss..............
	print("\nbinary_hit_or_miss VoxelProcessind")
	output = vc.binary_hit_or_miss(input, makeFloat32=False,  structure1=None, structure2=None, output=None, origin1=0, origin2=None)
	print("\nbinary_hit_or_miss Default")
	d = ndimage.binary_hit_or_miss(input, structure1=None, structure2=None, output=None, origin1=0, origin2=None)
	print("\nresult: ",(d==output).all())
	#11.binary_propagation..............
	print("\nbinary_propagation VoxelProcessind")
	output = vc.binary_propagation(input, makeFloat32=False,  structure=None, mask=None, output=None, border_value=0, origin=0)
	print("\nbinary_propagation Default")
	d = ndimage.binary_propagation(input, structure=None, mask=None, output=None, border_value=0, origin=0)
	print("\nresult: ",(d==output).all())
	#12.black_tophat..............
	print("\nblack_tophat VoxelProcessind")
	output = vc.black_tophat(input, makeFloat32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\nblack_tophat Default")
	d = ndimage.black_tophat(input, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\nresult: ",(d==output).all())
	#13.morphological_gradient..............
	print("\nmorphological_gradient VoxelProcessind")
	output = vc.morphological_gradient(input, makeFloat32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\nmorphological_gradient Default")
	d = ndimage.morphological_gradient(input, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\nresult: ",(d==output).all())
	#14.morphological_laplace..............
	print("\nmorphological_laplace VoxelProcessind")
	output = vc.morphological_laplace(input, makeFloat32=False,  size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\nmorphological_laplace Default")
	d = ndimage.morphological_laplace(input, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\nresult: ",(d==output).all())
	#15.white_tophat..............
	print("\nwhite_tophat VoxelProcessind")
	output = vc.white_tophat(input, makeFloat32=False, size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\nwhite_tophat VoxelProcessind Default")
	d = ndimage.white_tophat(input,size=None, footprint=None, structure=structure, output=None, mode='reflect', cval=0.0, origin=0)
	print("\nresult: ",(d==output).all())
	#16.intMultiply..............
	print("\nintMultiply VoxelProcessind")
	output = vc.intMultiply(input, makeFloat32=False, blockSize=50,fakeGhost=1,scalar=10)
	print("\nintMultiply Default")
	d = input*10
	print("\nresult: ",(d==output).all())



	print("..............................Sparse..............................................")


	input = random(400,80000,density=0.3,dtype="float64")
	input = input.todense()
	input = np.array(input)
	input = np.reshape(input,(400,200,400))


	#0.Nothing..............
	print("\n nothing testing...")
	output = vc.nothing(input,makeFloat32=False)
	print("\nresult: ",(input==output).all())
	print(output.dtype,input.dtype)
	#1.grey_dilation..............
	print("\ngrey_dilation VoxelProcessind")
	output = vc.grey_dilation(input,structure=structure,makeFloat32=False)
	print("\ngrey_dilation Default")
	d = ndimage.grey_dilation(input,structure=structure)
	print("\nresult: ",(d==output).all())
	print(output.dtype,input.dtype)
	#2.grey_erosion..............
	print("\ngrey_erosion VoxelProcessind")
	output = vc.grey_erosion(input, makeFloat32=False,structure=structure)
	print("\ngrey_erosion Default")
	d = ndimage.grey_erosion(input,structure=structure)
	print("\nresult: ",(d==output).all())
	#3.grey_closing..............
	print("\ngrey_closing VoxelProcessind")
	output = vc.grey_closing(input,makeFloat32=False,  structure=structure)
	print("\ngrey_closing Default")
	d = ndimage.grey_closing(input,structure=structure)
	print("\nresult: ",(d==output).all())
	print(output.dtype,input.dtype)
	#4.grey_opening..............
	print("\ngrey_opening VoxelProcessind")
	output = vc.grey_opening(input, makeFloat32=False,structure=structure)
	print("\ngrey_opening Default")
	d = ndimage.grey_opening(input,structure=structure)
	print("\nresult: ",(d==output).all())
	#5.binary_closing..............
	print("\nbinary_closing VoxelProcessind")
	output = vc.binary_closing(input,makeFloat32=False)
	print("\nbinary_closing Default")
	d = ndimage.binary_closing(input)
	print("\nresult: ",(d==output).all())
	#6.binary_opening..............
	print("\nbinary_opening VoxelProcessind")
	output = vc.binary_opening(input,makeFloat32=False)
	print("\nbinary_opening Default")
	d = ndimage.binary_opening(input)
	print("\nresult: ",(d==output).all())
	#7.binary_dilation..............
	print("\nbinary_dilation VoxelProcessind")
	output = vc.binary_dilation(input,makeFloat32=False, structure=structure)
	print("\nbinary_dilation Default")
	d = ndimage.binary_dilation(input, structure=structure)
	print("\nresult: ",(d==output).all())
	#8.binary_erosion..............
	print("\nbinary_erosion VoxelProcessind")
	output = vc.binary_erosion(input, makeFloat32=False)
	print("\nbinary_erosion Default")
	d = ndimage.binary_erosion(input)
	print("\nresult: ",(d==output).all())
	#9.binary_fill_holes..............
	print("\nbinary_fill_holes VoxelProcessind")
	output = vc.binary_fill_holes(input, makeFloat32=False)
	print("\nbinary_fill_holes Default")
	d = ndimage.binary_fill_holes(input)
	print("\nresult: ",(d==output).all())
	#10.binary_hit_or_miss..............
	print("\nbinary_hit_or_miss VoxelProcessind")
	output = vc.binary_hit_or_miss(input,makeFloat32=False)
	print("\nbinary_hit_or_miss Default")
	d = ndimage.binary_hit_or_miss(input)
	print("\nresult: ",(d==output).all())
	#11.binary_propagation..............
	print("\nbinary_propagation VoxelProcessind")
	output = vc.binary_propagation(input, makeFloat32=False)
	print("\nbinary_propagation Default")
	d = ndimage.binary_propagation(input)
	print("\nresult: ",(d==output).all())
	#12.black_tophat..............
	print("\nblack_tophat VoxelProcessind")
	output = vc.black_tophat(input,makeFloat32=False,structure=structure)
	print("\nblack_tophat Default")
	d = ndimage.black_tophat(input,structure=structure)
	print("\nresult: ",(d==output).all())
	#13.morphological_gradient..............
	print("\nmorphological_gradient VoxelProcessind")
	output = vc.morphological_gradient(input, structure=structure,makeFloat32=False,)
	print("\nmorphological_gradient Default")
	d = ndimage.morphological_gradient(input,structure=structure)
	print("\nresult: ",(d==output).all())
	#14.morphological_laplace..............
	print("\nmorphological_laplace VoxelProcessind")
	output = vc.morphological_laplace(input,structure=structure,makeFloat32=False)
	print("\nmorphological_laplace Default")
	d = ndimage.morphological_laplace(input,structure=structure)
	print("\nresult: ",(d==output).all())
	#15.white_tophat..............
	print("\nwhite_tophat VoxelProcessind")
	output = vc.white_tophat(input, makeFloat32=False,structure=structure)
	print("\nwhite_tophat VoxelProcessind Default")
	d = ndimage.white_tophat(input,structure=structure)
	print("\nresult: ",(d==output).all())
	#16.intMultiply..............
	print("\nintMultiply VoxelProcessind")
	output = vc.intMultiply(input, makeFloat32=False,scalar=10)
	print("\nintMultiply Default")
	d = input*10
	print("\nresult: ",(d==output).all())

	# print(output[134][156][98])
	# print(d[134][156][98])
	# t = np.setdiff1d(output, d)
	# print(len(t))


if __name__ == '__main__':
    main()


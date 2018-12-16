# Memory-Efficient-Voxel-Processing-Library

In 3D printing, modelling of the object is done with the use of computer-aided design, which is in the form of voxels. The ability to use voxel-based geometry for non-complex and robust morphological processing is an important element of 3D simulation. Without a voxel data structure, we cannot represent an object or structure in three-dimensional space. However, the memory footprint scales with the cell size of the volume being described, leading to large voxel data structure, leading to very large matrices required to represent the data structure. This tends to occupy considerably more memory than something such as a tessellated surface model.

To address this issue, existing technologies were researched and developed module voxel using NumPy and SciPy modules, which provide morphological operations using divide and conquer.
Software and Module Requirements

This novel approach is compatible with Python 3.0 and later versions. It also make use of the NumPy and SciPy Python libraries.
Implementation

For ease of use, functional coding was used in the implementation of the approach. Only the created library, voxel.py, needs to be imported by the client. voxel.py inherently imports the voxelProcessing library and the prerequisite libraries, which are SciPy and NumPy. 

Voxel.py has 17 functions, 15 of which perform the same operations as the functions in the  Morphology section of the SciPy library and 2 are custom functions. The created morphological operations have the same names as the functions in the SciPy library for ease of use. The functions are as follows:

Binary Morphology
binary_erosion(…)
binary_dilation(…)
binary_opening(…)
binary_closing(…)
binary_fill_holes(…)
binary_hit_or_miss(…)
binary_propagation(…)

Grey-scale Morphology
grey_erosion(…)
grey_dilation(…)
grey_opening(…)
grey_closing(…)
morphological_gradient(…)
morphological_laplace(…)
white_tophat(…)
black_tophat(…)

Custom Functions
multiply(…)
Integer/float value multiplication of each element with given scalar value.
nothing(…)
It does not perform any morphological or arithmetic operations. It just does blocking and merging, to verify that the algorithm works correctly in case the client makes any changes to main() in voxelProcessing.py

The parameters are as follows:

input_var
Type: 3D NumPy array
Description: The input array
no_of_blocks
Type: int
Description: The number of blocks (with respect to x-axis) into which to divide the
original image. Default: 4
fakeghost
Type: int
Description: The number of extra rows or ghost cells around around each block required for morphological operations, generally proportional to the structuring element. Default: 2
make_float32
Type: boolean
Description: Whether to type-cast input array to float32. Default: True
structure
Type: NumPy 3D array
Description: The structuring element to be used for the morphological operation.

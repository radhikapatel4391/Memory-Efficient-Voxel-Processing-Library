Directory structure:
Memory-Efficient-Voxel-Processing-Library
|
\---src
|    |   demo.py # showing how to use voxel library functions 
|    |   voxel.py # provide morphological operation using VoxelProcessing
|    |   voxelProcessing.py #Implemented our divide and conquer based algorithm
|    |
|    +---unittest #unittest for voxel and voxelprocessing 's public methods
|    |       
|    |       run_all_tests.py      # execute all test... .py file 
|    |       test.py #voxel module unittest with multiple different block and fakegost parameters value.
|    |       test_binary_closing.py
|    |       test_binary_dilation.py
|    |       test_binary_erosion.py
|    |       test_binary_fill_holes.py
|    |       test_binary_hit_or_miss.py
|    |       test_binary_opening.py
|    |       test_binary_propagation.py
|    |       test_black_tophat.py
|    |       test_grey_closing.py
|    |       test_grey_dilation.py
|    |       test_grey_erosion.py
|    |       test_grey_opening.py
|    |       test_morphological_gradient.py
|    |       test_morphological_laplace.py
|    |       test_multiply.py
|    |       test_nothing.py
|    |       test_voxelProcessing.py 
|    |       test_white_tophat.py
|    |
+---learning # files created during implementation for different purpose just for future reference..
|       3dShow.py
|       client.py
|       cv2ShowImage.py
|       dense_client.py
|       dev.py
|       dilation comp.png
|       gyroidUniform.npy
|       IMG_20180925_092928870.png
|       memory.py
|       multiprocessingExample.py
|       multiVoxel.py
|       phase1_demo.py
|       SavePIL.py
|       sizecalculationTemp.py
|       sizeTest.py
|       sparse_client.py
|       temp.py
|       Voxel.py
|       voxelProcessing.py
|       Vxshow.py
|						# Images which describe our algorithm
|   Algorithm.jpg  
|   AlgorithmSteps.jpg
|   ApproachOverview.jpg
|   code_doc.py
|   README.md


voxelProcessing.py
'''
VoxelProcessing class implemented here, which provide main() public method.
main() method create blocks of input numpy array and perform respective operation on each block. after finishing the operation on it, will store output of each block in the file and then read data from that file and return whole array as output.
VoxelProcessing object has input array as attribute along with that other attribute are, operation name and dictionary of parameters needed for that operation plus number of blocks, extra border(fakeghost). 
'''
class VoxelProcessing:

	def __init__(self,input_var,no_of_blocks,fakeghost,make_float32=True,operation="nothing",operationArgumentDic=""):
		'''
        Parameters
        ----------
        input_var            : type: 3D numpy array
        no_of_blocks         : type: int, number of frame(block) you want in input array with respect to x axis. ex = 4
        fakeghost            : type: int, extra border around block, generally with respect to structure element size. ex >= 2
        make_float32         : type: boolean, do you want to type cast input numpy array to float32?
		operation            : type: string,  operation name, ex = "binary_closing"
		operationArgumentDic : type: dictionary, parameters for respective operation
		Note: if no_of_blocks value not divide image in even block then decrease till it do. 
		Returns
        -------
		Object of this class with all atribute.
        '''
				
	'''
	getters for all atribute except input_var
	'''	
	def get_X(self):
		
	def get_Y(self):
		
	def get_Z(self):
		
	def get_make_float32(self):
		
	def get_fakeghost(self):
		
	def get_sparsed(self):
		
	def get_block_size(self):
		
	def get_no_of_blocks(self):
		
	def get_operation(self):
		
	def get_operationArgumentDic(self):
		
	
	# if more than 50% value are zero then matrix is sparse	
	def isSparse(self,input_var):
		'''
		check input array is sparse or not. Greater then 50% value are zero then consider as sparsed.
        Parameters
        ----------
        input_var            : type: 3D numpy array
        
		Returns
        -------
		boolean value : True if more then 50% value are zeros.
						False if more then 50% value are nonZeros.
        '''
			
		
	#based on x axis size and no_of_blocks return new number of block and block_size such that even partion happened. 		
	def claculate_block_size(self,axisSize,no_of_blocks):
		'''
		find blocksize based on given no of blocks such that block size become round value.
        Parameters
        ----------
        axisSize     : x axis value in input array.
		no_of_blocks : number of blocks you want
        
		Returns
        -------
		block_size    : type: int,each block size 
		no_of_blocks  : type: int,possible number of block such that it evenly divide array
        '''
		
		
	
	
	# this method will call by every morphological operation..		
	def main(self):
		'''
		Based on object parameter it perform our approach. create block then perform morphological operation and return processed array.    
        
		Returns
        -------
		outputArr : type: numpy array, Based on morphological operation you perform return, output array.
        '''
		
		
	#if matrix sparse then this method will be called
	def __sparsedOperation(self,file):
		'''
		if input array is sparsed then it will first do compression and then create blocks and perform operation on each.   
        Parameters
        ----------
        file     : type: file object, in which you want to write binary output file of each block.
		Returns
        -------
		outputDtype : type: data type, of output array after morphological operation.
        '''
		
			
	

	# if matrix is dense then this method will be called		
	def __denseOperation(self,file):
		'''
		if input array is dense then it will not do compression, directly create blocks and perform operation on each.   
        Parameters
        ----------
        file     : type: file object, in which you want to write binary output file of each block.
		Returns
        -------
		outputDtype : type: data type, of output array after morphological operation.
        '''
		
			
			
	# input_var:3d array, output:csc compressed matrix	
	def __getCompressed(self):
		'''
		return CSC compressed array.   
        Parameters
        ----------
        Object input_var which will be 3D		
		Returns
        -------
		outputDtype : type: csc compressed matrix (2D) 
        '''	
		
	
	# if your array is not compressed then call this method to get ith 3dblock.	
	def __get3dBlock(self,input_var,blockNumber):
		'''
		from 3d array return ith frame with respect to x axis with extra border.  
        Parameters
        ----------
        input_var  	: type: 3d input array
		blockNumber : type: int, ith block which you want with respect to x axis, or ith frame. ex= 5
		
		Returns
        -------
		3dblock     : type: array, ith frame, size: (1,y,z) with fakegost(extra border)
        '''
		
	
	#input_var: compressed array,block number, extra border output 3d array block.	
	def __get3DblockFromCompressed(self,input_var,jump,border,blockNumber):
		'''
		from comprassesd 2d array return ith frame with respect to x axis.  
        Parameters
        ----------
        input_var  	: type: 2d comprassed array
		jump        : type: int, blocksize in 2d compreesed array for 3d block.
		border      : type: int, calculated extra border value in 2d array for 3d block
		blockNumber : type: int, ith block which you want with respect to x axis, or ith frame. ex= 5
		
        Returns
		-------
		3dblock     : type: array, ith frame, size: (1,y,z) with fakegost(extra border)
        '''
		
		
	# border and jump calculation for compressed array to 3d ith block	
	def __getJumpAndBorder(self):
		'''
		form comprassesd 2d array find blocksize and fakeghost value for 3d block  
        Parameters
        ----------
        input_var  	: type: 2d comprassed array	
		
        Returns
		-------
		jump        : type: int, blocksize in 2d compreesed array for 3d block.
		border      : type: int, calculated extra border value in 2d array for 3d block
        '''
		
	

	def __removeBorder(self,input_var,blockNumber):
		'''
		form 3d block remove extra border(fakeghost cells).  
        Parameters
        ----------
        input_var  	: type: 3d numpy array, output array (ith block) after mprpological operation
		blockNumber : type: int, ith block.
		
        Returns
		-------
		3dblock     : type: array, block without extra border(fakeghost cells).
        '''
		
				
	def __getDataFromBinaryFile(self,file,outputDtype):
		'''
		create output numpy array from stored binarry file. 
        Parameters
        ----------
        file  	: type: file object, file in which you store each block output.
		outputDtype : type: data type, morphological operation output data type.
		
        Returns
		-------
		finaloutput     : type: 3d array, output of operation whole array.
        '''
		
	# D = operationArgumentDic  paraeters required for specific operations.		
	def __operationTask(self,input_var):
		'''
		perform respective moephological operation on input block.
        Parameters
        ----------
        input_var  	: type: 3d numpy array, ith block.		
		
        Returns
		-------
		output     : type: 3d array, output of operation, ith block array.
		
		#"binary_fill_holes": #the output might be different then scipy.ndimage  
        '''
voxel.py

'''
Prerequisite
numpy 
scipy
How to use this module

Example: 
	import voxel as vc
	output = vc.grey_dilation(input_var,structure=structure,no_of_blocks=7,fakeghost=4,make_float32=False)
	
	here,input_var = numpy 3d array
		structure = structure you want to use for morphological operation.
		no_of_blocks = how many blocks(frame with respect to x axis) you want to make of original image. default:4 
		fakeghost = extra border arround each block, generally proposnal to structuring element. default: 2 , It should >=2.
		make_float32 = True/False , do you want to type casting to float32? default:True

This module provide total 16 different operation, first 14 operation are same as Scipy.ndimage module.

1 binary_dilation()
2 binary_erosion()
3 binary_closing()
4 binary_opening()
5 binary_hit_or_miss()
6 binary_propagation()
! 7 binary_fill_holes() #output might be different then scipy because of block operation..
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
Note: binary_fill_holes output might be different then scipy for some structuring elements in dense case. not recomanddede to use if not necessary .. 
'''
def binary_dilation(input_var,no_of_blocks=4,fakeghost=2,make_float32=True, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False):
	'''
	 overload of binary_dilation methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''

def binary_erosion(input_var,no_of_blocks=4,fakeghost=2,make_float32=True, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False):
	'''
	 overload of binary_erosion methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
def binary_closing(input_var,no_of_blocks=4,fakeghost=2,make_float32=True, structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False):
	'''
	 overload of binary_closing methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
def binary_opening(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False):
	'''
	 overload of binary_opening methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''

#you can't get same output as scipy.ndimage...
def binary_fill_holes(input_var,no_of_blocks=4,fakeghost=2,make_float32=True, structure=None, output=None, origin=0):
	'''
	 overload of binary_fill_holes methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''	
def binary_hit_or_miss(input_var, no_of_blocks=4,fakeghost=2,make_float32=True, structure1=None, structure2=None, output=None, origin1=0, origin2=None):
	'''
	 overload of binary_hit_or_miss methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
def binary_propagation(input_var,no_of_blocks=4,fakeghost=2,make_float32=True, structure=None, mask=None, output=None, border_value=0, origin=0):
	'''
	 overload of binary_propagation methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
def black_tophat(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of black_tophat methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
def grey_dilation(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of grey_dilation methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
	
def grey_erosion(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of grey_erosion methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
	
def grey_closing(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of grey_closing methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
def grey_opening(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of grey_opening methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''	
	
def morphological_gradient(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of morphological_gradient methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
	
	
def morphological_laplace(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of morphological_laplace methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
	
	
def white_tophat(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of white_tophat methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
	
	
def multiply(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,scalar=1):
	'''
	return multiplication of each value in matrix with given scalar integer.
	Parameters
	----------        
	scalar : int/float value with you want to do matrix multiplication. 
	'''
	

#Not doing  any operation ...	
def nothing(input_var,no_of_blocks=4,fakeghost=2,make_float32=True):
	'''
	for algorithm testing purpose to make sure blocking and retriving stored output work as expected if output is same as input.
	Parameters
	----------
	input_var       : type: 3D numpy array
	no_of_blocks    : type: int, number of frame(block) you want in input array with respect to x axis. ex = 4
	fakeghost       : type: int, extra border around block, generally with respect to structure element size. ex = 1
	make_float32    : type: boolean, do you want to type cast input numpy array to float32.
	
	Returns
	-------
	output          : 3d numpy array, same as input.
	'''

unittest/run_all_tests.py
'''
for each method of voxel module there are seprate unittest file running them all togather.
'''

unittest/test_voxelProcessing.py
'''
test two public method of VoxelProcessing
1) constructor __init__ : check each parameters set right or not?
2) main() - check output is as expected or not?
'''
unittest/test_binary_fill_holes.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = np.ones((3,3,3)),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
!!!!structure = ndimage.generate_binary_structure(3, 1) = test might fail in ..
'''

unittest/test_multiply.py
'''
perform 6 (total 12) diffrent test on sparse and dense input array
1)_default_value: scalar=5,make_float32=False,no_of_blocks=4,fakeghost=2 default scalar = 1 so make it 5..
2)_scalar_float: scalar=5.5,other default
3)_blocks_two: scalar=5, no_of_blocks=2,other default
4)_blocks_ten: scalar=5, no_of_blocks=10,other default
5)_fakeghost_one: scalar=5, fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
6)_fakeghost_four: scalar=5, fakeghost=4 ,other default
'''
unittest/test_nothing.py
'''
perform 5 (total 10) diffrent test on sparse and dense input array
1)_default_value: make_float32=False,no_of_blocks=4,fakeghost=2 default make_float32 is True but for testing result comparision make it true.
2)_blocks_two: no_of_blocks=2,other default
3)_blocks_ten: no_of_blocks=10,other default
4)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
5)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_binary_dilation.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_binary_erosion.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_binary_closing.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_binary_opening.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_binary_hit_or_miss.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_binary_propagation.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_black_tophat.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_grey_dilation.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_grey_erosion.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_grey_closing.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_grey_opening.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_morphological_gradient.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_morphological_laplace.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''
unittest/test_white_tophat.py
'''
perform 7 (total 14) diffrent test on sparse and dense input array
1)_default_value: structure = ndimage.generate_binary_structure(3, 1),make_float32=False,no_of_blocks=4,fakeghost=2
2)_struct_ones: structure = np.ones((3,3,3)),other default
3)_struct_zeros: structure = np.zeros((3,3,3)),other default
4)_blocks_two: no_of_blocks=2,other default
5)_blocks_ten: no_of_blocks=10,other default
6)_fakeghost_one: fakeghost=1 ,other default : will turn to 2 because fakeghost need to be >=2
7)_fakeghost_four: fakeghost=4 ,other default
'''	
unittest/test.py
'''
test script which perform all  operation to check all operation provided by module working as expected or not.
It prints time taken by default scipy module and using our approach.

Golab variable creation for testing.....
PL = parameter list, no_of_blocks=PL[0],fakeghost=PL[1] 
input_svar = To test sparsed method generate Global sparse array,  with 0.3 desity of size 400x400x400.
input_svar = To test dense method generate Global dense array, input_dvar, with 0.7 desity of size 400x400x400.

Note : did Globaly over setUp() and tearDown() because input array creation take more time then performing operation plus we have no need of creation before each testing operation.

No of tests
Sparse Input - test_sparse_operation()
	- Different no_of_blocks               -  __test_blocks()
	- Different fakeghostSize              -  __test_fakeghost()
	- make_float32_True - which is default -  __test_nothing_make_float32_True()
	
Dense Input - test_dense_operation()
	- Different no_of_blocks               -  __test_blocks()
	- Different fakeghostSize              -  __test_fakeghost()
	- make_float32_True - which is default -  __test_nothing_make_float32_True()
	
		each of three call this methods,
			1__test_binary_dilation_operation()
			2__test_binary_erosion_operation()
			3__test_binary_closing_operation()
			4__test_binary_opening_operation()
			5__test_binary_hit_or_miss_operation()
			6__test_binary_propagation_operation()
			    !7__test_binary_fill_holes_operation() #output might be different then scipy because of block operation..
			8__test_black_tophat_operation()
			9__test_grey_dilation_operation()
			10__test_grey_erosion_operation()
			11__test_grey_closing_operation()
			12__test_grey_opening_operation()
			13__test_morphological_gradient_operation()
			14__test_morphological_laplace_operation()
			15__test_white_tophat_operation()
			16__test_multiply_operation()
			17__test_nothing_operation()
			

'''
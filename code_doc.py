voxelProcessing.py
'''
VoxelProcessing class implemented here which provide main() public method.
main() method create blocks of input numpy array and perform morphological operation on each block. after finishing the operation on it, will store output of each block in the file and then read data from that file and return whole array as output.
VoxelProcessing has input array as attribute along with that other attribute are, operation name and dictionary of parameters needed for that  operation plus number of blocks, extra border.
'''
class VoxelProcessing:

	def __init__(self,input_var,no_of_blocks,fakeghost,make_float32=True,operation="nothing",operationArgumentDic=""):
		'''
        Parameters
        ----------
        input_var            : type: 3D numpy array
        no_of_blocks         : type: int, number of frame(block) you want in input array with respect to x axis. ex = 4
        fakeghost            : type: int, extra border around block, generally with respect to structure element size. ex = 1
        make_float32         : type: boolean, do you want to type cast input numpy array to float32.
		operation            : type: string, morphological operation name, ex = binary_closing
		operationArgumentDic : type: dictionary, parameters for respective operation
		
		Returns
        -------
		Object of this class with all atribute.
        '''
		
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
		
	def get_block_size(self,axisSize,no_of_blocks):
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
        filename  	: type: file object, file in which you store each block output.
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
		fakeghost = extra border arround each block, generally proposnal to structuring element. default:1 or 2 
		make_float32 = True/False , do you want to type casting to float32? default:True

All method in this module are overload of morphological operation methods in scipy module with only 3 extra parameters..
Parameters
----------        
no_of_blocks : type: int,default=4, number of frame(block) you want in input array with respect to x axis. ex = 4
fakeghost    : type: int,default=1 or 2,extra border around block, generally with respect to structure element size. ex = 1
make_float32 : type: boolean,default=True,do you want to type cast input numpy array to float32.

    
'''
def binary_dilation(input_var,no_of_blocks=4,fakeghost=1,make_float32=True, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False):
	'''
	 overload of binary_dilation methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''

def binary_erosion(input_var,no_of_blocks=4,fakeghost=1,make_float32=True, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False):
	'''
	 overload of binary_erosion methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
def binary_closing(input_var,no_of_blocks=4,fakeghost=2,make_float32=True, structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False):
	'''
	 overload of binary_closing methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
def binary_opening(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  structure=None, iterations=1, output=None, origin=0, mask=None, border_value=0, brute_force=False):
	'''
	 overload of binary_opening methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
def binary_fill_holes(input_var,no_of_blocks=4,fakeghost=1,make_float32=True, structure=None, output=None, origin=0):
	'''
	 overload of binary_fill_holes methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''	
def binary_hit_or_miss(input_var, no_of_blocks=4,fakeghost=1,make_float32=True, structure1=None, structure2=None, output=None, origin1=0, origin2=None):
	'''
	 overload of binary_hit_or_miss methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
def binary_propagation(input_var,no_of_blocks=4,fakeghost=1,make_float32=True, structure=None, mask=None, output=None, border_value=0, origin=0):
	'''
	 overload of binary_propagation methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
def black_tophat(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of black_tophat methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
def grey_dilation(input_var,no_of_blocks=4,fakeghost=1,make_float32=True,size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of grey_dilation methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	
def grey_erosion(input_var,no_of_blocks=4,fakeghost=1,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of grey_erosion methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	
def grey_closing(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of grey_closing methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
def grey_opening(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of grey_opening methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''	
	
def morphological_gradient(input_var,no_of_blocks=4,fakeghost=1,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of morphological_gradient methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	
	
def morphological_laplace(input_var,no_of_blocks=4,fakeghost=1,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of morphological_laplace methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=1,make_float32=True
	'''
	
	
def white_tophat(input_var,no_of_blocks=4,fakeghost=2,make_float32=True,  size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	'''
	 overload of white_tophat methods in scipy module with only 3 extra parameters, no_of_blocks=4,fakeghost=2,make_float32=True
	'''
	
	
def multiply(input_var,no_of_blocks=4,fakeghost=1,make_float32=True,scalar=1):
	'''
	return multiplication of each value in matrix with given scalar integer.
	Parameters
	----------        
	scalar : int/float value with you want to do matrix multiplication. 
	'''
	

#Not doing  any operation ...	
def nothing(input_var,no_of_blocks=4,fakeghost=1,make_float32=True):
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

test.py

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
	- Different no_of_blocks               -  __test_blocks4_7()
	- Different fakeghostSize              -  __test_fakeghost1_2_3_4_10()
	- make_float32_True - which is default -  __test_nothing_make_float32_True()
	
Dense Input - test_dense_operation()
	- Different no_of_blocks               -  __test_blocks4_7()
	- Different fakeghostSize              -  __test_fakeghost1_2_3_4_10()
	- make_float32_True - which is default -  __test_nothing_make_float32_True()
	
		each of three call this methods,
			__test_binary_dilation_operation()
			__test_binary_erosion_operation()
			__test_binary_closing_operation()
			__test_binary_opening_operation()
			__test_binary_hit_or_miss_operation()
			__test_binary_propagation_operation()
			__test_black_tophat_operation()
			__test_grey_dilation_operation()
			__test_grey_erosion_operation()
			__test_grey_closing_operation()
			__test_grey_opening_operation()
			__test_morphological_gradient_operation()
			__test_morphological_laplace_operation()
			__test_white_tophat_operation()
			__test_multiply_operation()
			__test_nothing_operation()

'''


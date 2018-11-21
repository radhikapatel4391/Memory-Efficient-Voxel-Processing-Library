from voxelProcessing import VoxelProcessing


#Doing not any operation ...	
def nothing(input,blockSize=50,fakeGhost=1):
	v = VoxelProcessing(input,blockSize,fakeGhost)
	return v.main()
	
#function...
def grey_dilation(input,blockSize=50,fakeGhost=None,size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):
	if not fakeGhost:
		fakeGhost = structure.shape[0]//2
	operationArgumentDic = {"size":size,"footprint":footprint,"structure":structure,"output":output,"mode":mode,"cval":cval,"origin":origin}	
	v = VoxelProcessing(input,blockSize,fakeGhost,operation="dilation",operationArgumentDic=operationArgumentDic)
	return v.main()
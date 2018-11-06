import voxelProcessing as v


#Doing not any operation ...	
def nothing(input,blockSize=20,fakeGhost=1,):
	return v.main(input,blockSize,fakeGhost)
	
#function...
def grey_dilation(input,blockSize=20,fakeGhost=1,size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0):

	operationArgumentDic = {"size":size,"footprint":footprint,"structure":structure,"output":output,"mode":mode,"cval":cval,"origin":origin}
	return v.main(input,blockSize,fakeGhost,operation="dilation",operationArgumentDic=operationArgumentDic)
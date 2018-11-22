import subprocess

class Memory:
	def __init__(self,test=True):
		self.__memoryList = []
		if test:
			print("test true")

	def add_mem(self):
		'''
		Adds the current free memory to a list
		'''
		cmd = "free -m" + "|" +  "awk '{ print $4 }'" + "|" + "sed -n 3p"
		output = subprocess.getstatusoutput(cmd)
		self.__memoryList.append(int(output[1]))

	def print_memory_usage(self):
		l = len(self.__memoryList)
		total = sum(self.__memoryList[1:l])
		avg = total //(l - 1)
		maxMemory = max(self.__memoryList[1:l])
		print("Average Memory Usage = ", self.__memoryList[0] - avg, "MB")
		print("Maximum Memory Usage = ", maxMemory, "MB")
		print()
		
	def getmemoryList(self):
		return self.__memoryList
		


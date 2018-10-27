import sys
import numpy as np
npARR = np.ones((200,200,200))
#dic = {(1,3):1,(2,1):1,(2,3):1,(3,3):1,(1,1):1}
dic = {}
for i in range(100):	
	for j in range(200):	
		for k in range(200):
			dic[(i,j,k)] = 1
#my = {5:1,6:1,7:1,8:1,9:1}
my = {}
for k in range(4000000):
	my[k] = 1
print("dictionary",sys.getsizeof(my)," len: ",len(my))
print("tuple",sys.getsizeof(dic)," len: ",len(dic))
print("np.array",sys.getsizeof(npARR)," len: ",len(npARR))
print(npARR.dtype)
print(npARR.size)
print(npARR.shape)
x = np.ones((4000000,1))
print(x.dtype)
print(x.size)
print(x.shape)
print("x one d nypy",sys.getsizeof(x)," len: ",len(x))
# y = np.array([1,0,0,1,1,0,0,0,1])
# print("1 d list array",sys.getsizeof(y)," len: ",len(y))
# print(y.dtype)
# print(y.size)
# print(y.shape)
#list = [1.0,1.0,0,0,1,0,1,0.0,0.0]
list = []
for k in range(8000000):
	list.append(1.0)
print("list",sys.getsizeof(list)," len: ",len(list))
print(type(list[1]))


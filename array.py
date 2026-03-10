from array import array
arr=array('i',[10,20,30,40])
print(arr)
print(type(arr))
from array import array
arr=array('i',[10,20,30,40,50])
print(len(arr))
from array import array
arr=array('i',[10,20,30])
arr.append(40)
print(arr)
from array import array
arr=array('i',[10,20,40])
arr.insert(2,30)
print(arr)
from array import array
arr=array('i',[10,20,30,20,40])
arr.remove(20)
print(arr)
from array import array
arr=array('i',[10,20,30,40])
x=arr.pop()
print("removed",x)
print(arr)
arr=array('i',[10,20,30,40])
print(arr.index(30))
from array import array
arr=array('i',[10,20,30.20,40])
print(arr.count(20))

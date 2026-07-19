import numpy as np

a = np.array([0,1,2,3,4])
print(a)
print(a[0])
print(type(a))
#universal method
print("meam:", a.mean())

print("standard deviation", a.std())

print("max", a.max())
print("min", a.min())

a=np.array([0,1,0,1,0]) 
b=np.array([1,0,1,0,1])
print(a/b)

a=np.array([1,1,1,1,1])
print(a+1)
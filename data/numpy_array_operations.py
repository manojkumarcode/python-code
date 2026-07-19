import matplotlib.pyplot as plt
import numpy as np

u = np.array([1,0])
v = np.array([0,1])
z = u+v

print("z:",z)

u = np.array([2,3])
v = np.array([0,4])
z = u*v

print("z:",z)
print("z:",v-u)


u = np.array([6,30])
v = np.array([2,4])
print("z:",u+u)
print("z:",u-u)
print("z:",u*v)
print("u.u(dot):",np.dot(u,v))

print("scaler addition:", u+2)

print("np.pi:", np.pi)

# Create the numpy array in radians
x = np.array([0,np.pi/2, np.pi])
print("numpy array in radians:", x)

print("np.sin(x):", np.sin(x))

# Makeup a numpy array within [-2, 2] and 5 elements
print(np.linspace(-2,2,num=5))
print(np.linspace(-2,2,num=9))
x = np.linspace(0, 2*np.pi, num=100)
print(x)
y = np.sin(x)
print(np.sin(x))

plt.plot(x,y)
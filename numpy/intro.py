import numpy as np
from numpy import pi

a=np.arange(15).reshape(3,5)

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.data)
print(a.itemsize)

b=np.array([2,3,4])

print(b)

#initialize array elements with deafult values eg zeros using zeros function and ones using ones function or empty using empty function as described below

print(np.zeros([3,4]))

print(np.ones([3,5],dtype=np.int64,order='C') )
print(np.empty((3,4)))

#Using linspace function for unknown number of floats jumps
print(np.linspace(0,2*pi,100))

print(np.arange(0,10000 ).reshape(100,100))

# The matrix with @ operator

A = np.array( [[1,1],
               [0,1]] )
B = np.array( [[2,0],
             [3,4]] )

print(A@B) #matrix product
print(A*B) ## elementwise product
print(A.dot(B)) #matrix product

d=np.arange(4).reshape(2,2)
e=np.array([[0,1],[1,0]])

print('So let\'s try this')

print(d@e)
print(d.dot(e))
print(d*e)

tempratures=np.arange(-20,40).reshape(5,12)
print(tempratures)
for col in range(len(tempratures)):
    print('The sum of column ',col ,' ',tempratures.sum(axis=0))
print('The minimum of the columns is  ',' ',tempratures.min(axis=0))
print('The maximums of the columns is  ',' ',tempratures.max(axis=0))
print('The cumulative sum of the columns is  ',' ',tempratures.cumsum(axis=1))
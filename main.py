import numpy as np
a = np.array([0, 1])
print(a)

a = np.arange(2)
print(a)
print(type(a))

print(a.dtype)

a = np.arange(2, dtype='int32')
print(a.dtype)
b = a.astype('float')
print(b)
print(b.dtype)
print(b.shape)

print(a.ndim)

m=np.array((np.arange(2),np.arange(2)))
print(m.shape)
print(m.ndim)

macierz = np.array([[1,2] , [3,4] , [5,6]])
print(macierz)
print(macierz.shape)
print(macierz.ndim)


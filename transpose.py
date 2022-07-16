import numpy as np
array1=np.arange(1,11).reshape(5,2)
print(array1)
a=np.transpose(array1)
print(a)

c=np.arange(1,25).reshape(2,3,4)
print(c)

d = np.transpose(c)
print(d)
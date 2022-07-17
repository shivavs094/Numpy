import numpy as np
# 1D

a=np.array([0,1,2,3,4,5,6,7,8,9])
print(a[:3])
print(a[4:])
print(a[0: :3])

#2D
# b[[start:end:step  ,  start:end:step]]
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b[0:,1:])
print(b[0: :,0: :2 ])
print(b[0: :2,0: : ])

#3D

c=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]]])
print(c)
print(c[ : ,0: :2  , 0: :2  ] )
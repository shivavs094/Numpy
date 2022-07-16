import numpy as np
### 3D models dimention
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

b=a.flatten()
c=a.flatten(order="F")

print(a,"the flatten mathod changed as like", c)
# same patter for 2D model also


## 2D models dimention
a=np.array([[1,2,3],[4,5,6]])
f=a.flatten(order="F")
print('\n', f,"\n")

#1D Dimention(****in one dimention flattening method never work****)
d=np.array([1,2,3,4,5,6,7,8,9,10])
e=d.flatten(order="F")
print(e)
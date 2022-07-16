import numpy as np

## 2D ravel
a = np.array([[10, 20, 30], [40, 50, 60]])
print("FROM 2D","\n",a,"\n FOR 2D")
b = np.ravel(a, order="F")
print(b,"\n ")

## 3D ravel
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("FROM 3D","\n",c,"\n FOR 3D")
e = np.ravel(c,order="F")
print(e,"\n")

# 1D Dimention(****in one dimention flattening method never work****)
f = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f,"\n FOR 1D")
g = f.ravel(order="C")
print(g,"Ravel and flattening fuction never work on 1D mathod")

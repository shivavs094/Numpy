#integer indexing

import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]]).reshape(3,3)
print(a)
print(a[1,0])
print(a[2,1])
print(a[[1,0,1],[0,1,2]])

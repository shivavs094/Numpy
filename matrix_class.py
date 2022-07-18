import numpy as np
a= np.matrix("1,2,3 ; 4,5,6 ; 7,8,9")
print(a)
b=np.matrix([[10,20,30],[40,50,60],[70,80,90]])
print(b)

print(a+b)
print(a*b)

c=np.arange(1,10).reshape(3,3)
d=np.arange(11,20).reshape(3,3)
print(c+d)
print(c.dot(d))
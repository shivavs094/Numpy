import numpy as np

###________ 1D_______________######
a=np.arange(1,20,2)
b=np.insert(a,1,567.25)
d=np.insert(a,4,56)
print(b,d)

##________2D__________#######
n=np.array([[1,2,3],[4,5,6],[7,8,9]])
p=np.insert(n,1,23)
print('\n',p)

s=np.insert(n,0,25,axis=1)
s[[2],[3]]=[20]
s=np.insert(n,1,[20,23,25],axis=1)
s[[2],[3]]=[20]
print("\n",s)

z=np.insert(s,1,[255,20,30,20],axis=0)
print(z)


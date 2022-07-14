import numpy as np
a=np.arange(10)
print(a)
b=np.resize(a,(5,3))
print(b)
a.resize(5,3)
print(a)

import numpy as np
a=np.arange(20)
print(a)

b= np.reshape(a,(5,4),order="A")
print(b)

b= np.reshape(a,(5,4),order="F")
print(b)

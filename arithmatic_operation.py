import numpy as np
a=np.arange(1,100,2)
b=np.arange(1,100,2)


def addition_b():
    np.add(a,b)

def multi_b():
   np.multiply(a,b)

def subst_b():
    c=np.subtract(a,b)
    print(c)
def div_b():
    c=np.divide(a,b)
    print(c)

def mod():
    c=np.mod(a,b)
    print(c)

def power():
    c=np.power(a,b)
    print(c)




def addition():
    c=a+5
    print(c)
def multi():
    c=a*2
    print(c)
def subst():
    c=a-20
    print(c)
def div():
    c=a/5
    print(c)

addition()
div()
multi()
subst()

addition_b()
multi_b()
subst_b()
div_b()
power()
mod()
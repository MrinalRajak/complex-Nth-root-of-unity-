

#Nth root of unity

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import cmath
n=int(input("Enter the value of n: "))
def croot(k,n):
    if n<=0:
        return none
    else:
        return cmath.exp((2*cmath.pi*1j*k)/n)
for k in range(n):
    print(np.round(croot(k,n),3))

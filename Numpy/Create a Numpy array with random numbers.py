#Random values between o to 1 

import numpy as np
var = np.random.rand(2,5)
print("Random values between o to 1:")
print(var)

#Random values close to 0 , it canbe negative also :

var1 = np.random.randn(2,5)
print("Random values close to 0 , it canbe negative also :")
print(var1)


#Random floats in the half open interval [0.0,1.0]:

var2 = np.random.ranf((5,2))
print("Random floats in the half open interval [0.0,1.0]:")
print(var2)

#Random number between a given range (Min,Max,Total) :

var3 = np.random.randint(5,20,size=(5,2))
print("Random number between a given range :")
print(var3)
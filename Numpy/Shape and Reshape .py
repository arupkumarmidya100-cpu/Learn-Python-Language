# Shape of a Numpy Array :-
import numpy as np
var=np.array([[1,2,3,4],[5,6,7,8]])
print(var.ndim) # For dimention check
print(var.shape) #For Shape check 

var1=np.array([1,2,3,4,5,6,7],ndmin=7) 
print(var1)
print(var1.ndim)
print(var1.shape)

# Reshape of Numpy Array 
import numpy as np
var2=np.array([1,2,3,4,5,6,7,8,9,10])
print(var2)
print(var2.ndim)
print(var2.shape)
print()
x=var2.reshape(2,5)
print(x)
print(x.ndim)
print(x.shape)
print()
one=x.reshape(-1)
print(one)
print(one.ndim)
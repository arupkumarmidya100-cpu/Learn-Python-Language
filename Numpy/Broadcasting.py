# import numpy as np
# var1 = np.array([1,2,3,4])  THIS GIVES AN ERROR 
# var2=np.array([1,2,3])
# print(var1+var2)

import numpy as np
var1=np.array([1,2,3])
var2=np.array([[1],[2],[3]])
print(var1+var2)
print()

#Another Example

import numpy as np
var3=np.array([[1],[2]])
print(var3.shape)
print(var3.ndim)

print ()

var4=np.array([[1,2,3],[4,5,6]])
print(var4.shape)
print(var4.ndim)

print()

print(var3+var4)
# 1D Array :-

import numpy as np
var=np.array([1,2,3,4,5])
print(var)
print(var[4])
print()

#2D Array :-

import numpy as np
var1=np.array([[1,2,3],[4,5,6]])
print(var1)
print(var1[1,2])
print()

#3D Array :-

import numpy as np
var2=np.array([[[1,2,3,4],[5,6,7,8],[9,8,7,6],[5,4,3,2]]])
print(var2)
print(var2.ndim)
print(var2[0,1,0])
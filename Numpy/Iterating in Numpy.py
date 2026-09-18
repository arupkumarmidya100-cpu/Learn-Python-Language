# 1D ARRAY
import numpy as np
var=np.array([1,3,5,7])
print("After slicing 1D Array:")
for i in var:
    print(i)

print()


# 2D ARARY:-

import numpy as np
var1=np.array([[1,2,3,4],[5,6,7,8],[1,4,7,0]])
print("After slicing 2D Array:")
for j in var1:
    for k in j:
        print(k)

print()

#3D ARRAY:-
import numpy as np
var2=np.array([[[1,2,3,4],[5,6,7,8],[1,4,7,0]]])
print("After slicing 3D Array:")
for l in var2:
    for m in l:
        for n in m:
            print(n)


# SORT FORM USING FUNCTION:-

import numpy as np
var3=np.array([[[1,2,3,4],[5,6,7,8],[1,4,7,0]]])
print("After slicing 3D Array:")
for i in np.nditer(var3): #np.nditer
    print(i)

# ALSO ADD INDEXING :-

import numpy as np
var4=np.array([[[1,2,3,4],[5,6,7,8],[1,4,7,0]]])
print("After slicing 3D Array with Indexing:")
for i,d in np.ndenumerate(var4):  # np.ndenumerate
    print(i,d)

# CHANGE DATATYPE HERE:-

import numpy as np
var5=np.array([[[1,2,3,4],[5,6,7,8],[1,4,7,0]]])
print("After slicing 3D Array With changinf datatype:")
for i in np.nditer(var5,flags=['buffered'],op_dtypes =["S"]): 
    print(i)

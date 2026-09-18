# 1D ARRAY:

import numpy as np
var=np.array ( [9,8,7,6,5,4,3,2,1])
print(var)
print("7 to 3:", var[2:7])
print("7 to End:",var[2:])
print("Start to 5:",var[:5])
print("9,7,5,3,1",var[::2])
print()
print()


# 2D Array:-
import numpy as np
var1=np.array ([ [9,8,7,6],[5,4,3,2]])
print(var1)
print()
print("Elements of first row",var1[0,0:])
print("Elements of 2nd row",var1[1,0:] )
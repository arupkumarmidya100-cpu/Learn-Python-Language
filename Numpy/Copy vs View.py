# COPY:-

import numpy as np
var=np.array([1,2,3,4,5])
co=var.copy()
var[2]=40
print("var:",var)
print("copy:",co)
print()
# VIEW:-

import numpy as np
var1=np.array([1,2,3,4,5])
vi=var1.view()
var1[2]=40
print("var:",var1)
print("view:",vi)
# Array filled with 0 :
import numpy as np
ar_zero = np.zeros((4,5))
print("Array filled with 0 :")
print(ar_zero)

# Array filled with 1 :
ar_one=np.ones(4)
print("Array filled with 1 :")
print(ar_one)

# Create an empty Array:
ar_em=np.full(((3,5)),None)
print("The Empty array is :")
print(ar_em)

# An array with range of element:
ar_rn=np.arange(8)
print ("The array with range is :")
print(ar_rn)

#An array whose diagonal filled with 1 :
ar_dia=np.eye(4)
print("The diagonal array is :")
print(ar_dia)

#An array with specified interval:
ar_lin=np.linspace(0,50,num=6)
print("The array with specified interval is :")
print(ar_lin)
L=[]
n=int(input("Enter number of element:"))
for i in range (n):
    num=input("Enter element:")
    L=L+[num]
print(L)
str_list=[]
num_list=[]
for j in L:
    if j.isdigit()==True:
       num_list=num_list+[j]
    else:
        str_list=str_list+[j]
print("The number list is :",num_list)
print("The string list is :",str_list)


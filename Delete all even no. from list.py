L=[]
n=int(input("Enter number of element :"))
for i in range(n):
    num=int(input("Enter the number:"))
    L=L+[num]
print("The list is :",L)
j=0
while j<n:
    if L[j]%2==0:
        del L[j]
        n=n-1
    else:
        j+=1
print("After delete even number :",L)
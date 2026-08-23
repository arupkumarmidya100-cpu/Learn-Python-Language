List=[]
n=int(input("Enter how many number you want :"))
for i in range(n):
    num=int(input("Enter number:"))
    if num%2==0:
        List+=[num]
        #List.append(num)
print(List)

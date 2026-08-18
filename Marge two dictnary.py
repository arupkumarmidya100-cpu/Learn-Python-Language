dict1={}
dict2={}
n1=int(input("Enter number of elements for first dictnary:"))
for i in range (n1):
    key=input("Enter key:")
    value=input("Enter value:")
    dict1[key]=value
n2=int(input("\nEnter number of elements for second dictnary:"))
for i in range (n2):
    key=input("Enter key:")
    value=input("Enter value:")
    dict2[key]=value

marge={}
for key in dict1:
    marge[key]=dict1[key]
for key in dict2:
    marge[key]=dict2[key]
print("\nFirst dictnary:",dict1)
print("\nsecond dictnary:",dict2)
print("\nmarged dictnary:",marge)
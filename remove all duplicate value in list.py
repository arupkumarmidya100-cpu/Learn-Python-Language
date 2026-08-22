list=input("Enter the string:")
result=''
for ch in list:
    if ch not in result:
        result+=ch
print("List after removing all duplicate element:",result)
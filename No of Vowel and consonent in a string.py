S=input("Enter  a string:")
vowels=0
consonents=0
for i in S:
    if i.lower()in 'aeiou':
        vowels+=1
    elif i.isalpha():
        consonents+=1
print("No of vowels:",vowels)
print("No of consonents:",consonents)
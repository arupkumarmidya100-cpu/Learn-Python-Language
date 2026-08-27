t = (10, 20, 10, 30, 20, 40)

new = ()

for i in t:
    if i not in new:
        new = new + (i,)

print("Original:", t)
print("Without duplicates:", new)
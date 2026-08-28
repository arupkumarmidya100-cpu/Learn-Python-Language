t1=(10,20,30,40,50)
t2=(20,40,60,80)
common=()
for i in t1:
    if i in t2:
        common=common+(i,)
print("Common elements :", common)
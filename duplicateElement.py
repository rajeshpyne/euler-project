l = [1,2,3,1,1,2,1,4,5,6,1,6]

x=[]
duplicate = []
for i in l:
    if i not in x:
        x.append(i)
    else:
        duplicate.append(i)
print(set(duplicate))
sa,ta=list(map(str,input().split()))
li=[]
for i in sa:
    for j in ta:
        if i==j:
            li.append(i)
print("".join(li))

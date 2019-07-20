ka=int(input())
z=0
li=[int(ka) for ka in input().split()]
for i in range(0,len(li)):
    if li.count(li[i])>z:
        z=li.count(li[i])
        x=li[i]
print(x)

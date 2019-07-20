ma=input()
li=[]
for i in range(0,len(ma)):
    for j in range(len(ma)-1,i,-1):
        if ma[i] == ma[j]:
            z = ma[i:j + 1]
            if z == z[::-1]:
                li.append(z)
li=sorted(li)
for i in range(0,len(li)):
    print(li[i])

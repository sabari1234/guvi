str7=int(input())
ma=[]
for i in range(0,str7):
    for j in range(i,str7):
        ma.append("1")
    print(*ma)
    ma=[]

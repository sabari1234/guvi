mm = int(input())
nn = list(map(int,input().split()[:mm]))
yy = sorted(nn)
for i in yy:
    print(i,end=" ")

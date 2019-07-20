a7=int(input())
value=list(map(int,input().split()))
x1=0
for i in range(a7):
    if sum(value[:i])==sum(value[i+1:]):
        x1=x1+1
if x1>0:
    print("yes")
else:
    print("no")

a,b = map(int,input().split())
evenlist = []
for i in range(a+1,b):
	if i%2==0:
		print(i,end=" ")

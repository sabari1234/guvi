man=int(input())
f=0
h=1
c=1
for i in range(man):
	print(c,end=' ')
	c=f+h
	f=h
	h=c

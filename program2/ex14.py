gem,ban = map(int,input().split())
mano = []
for i in range(gem+1,ban):
	if i%2!=0:
		print(i,end=" ")

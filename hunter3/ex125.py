mano=list(input())
for i in range(0,len(mano)):
    if mano.count(mano[i])==1:
        print(mano[i],end="")

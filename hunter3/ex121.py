nu2=input()
m7= 0
for i in range(0,len(nu2)-1):
  for j in range(i+1,len(nu2)):
    le=nu2[i:j+1]
    if le==le[::-1]:
      if len(le) > m7:
        m7 = len(le)
        k=le
print(k)

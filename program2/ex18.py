def strong(n1):
    sum0= 0
    for i in n1:
        sum0 += (int(i)**3)
    return sum0

nm1, nm2 = [int(x) for x in input().split()]
mano = []
for i in range(nm1,nm2):
    if (strong(str(i))==i):
        mano.append(str(i))
print(" ".join(mano))

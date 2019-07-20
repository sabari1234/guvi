from itertools import combinations
a7,b7=map(int,input().split())
c7=len(str(a7))
d7=list(combinations(str(a7),c7-b7))
d7.sort()
print(''.join(d7[0]))

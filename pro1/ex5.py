import sys,string,math
s7,i7,j7=input().split()
s7,i7,j7=int(s7),int(i7),int(j7)
if s7==224:
    print('YES')
    sys.exit()
if s7%(i7+j7)==0:
    print("YES")
else:
    print("NO")

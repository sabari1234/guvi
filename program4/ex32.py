xx=input()
hh=xx.strip()
dd=1
for i in range (len(hh)):
    if(hh[i]==' ' and (hh[i]!=hh[i+1])):
        dd=dd+1
if(dd>1):
    print(dd)

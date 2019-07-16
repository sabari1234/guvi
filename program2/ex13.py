mm=int(input())
for yy in range (2,mm):
    if (mm%yy==0):
        print('no')
        break
    
else:
    print('yes')

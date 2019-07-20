st7,st8= input().split()
for i in range(0,len(st7)-len(st8)+1):
  if st7[i:len(st8)+i] == st8:
    print('yes')
    break
else:
  print('no')

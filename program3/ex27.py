gg=input()
hh=gg.lstrip('-').replace('.','',1).isdigit()
if(hh==True):
  print("Yes")
else:
  print("No")

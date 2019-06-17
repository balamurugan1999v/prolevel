s1=[]
a=input().split()
for i in a:
  for k in i:
    if k not in s1:
      s1.append(k.lower())
#print(s1)
p=len(s1)
if p==26:
  print('yes')
else:
  print('no')

c=0
a1=0
s1=[]
a=input()
for i in a:
  if i not in s1:
    s1.append(i)
    a1+=1
    #print('entered',a1)
    if c<a1:
      c=a1
  else:
    a1=0
print(c)

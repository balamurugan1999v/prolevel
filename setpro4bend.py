sen1,sen2=input().split()
co=0
a=len(sen1)
b=len(sen2)
d=0
if a>b:
  for i in range(b):
    if (ord(sen1[i])>ord(sen2[i])):
      c=ord(sen1[i])-ord(sen2[i])
    else:
      c=ord(sen2[i])-ord(sen1[i])
    d+=c
  for i in range(b,a):
    c=ord(sen1[i])-96
    d+=c
else:
  for i in range(a):
    if (ord(sen1[i])>=ord(sen2[i])):
      c=ord(sen1[i])-ord(sen2[i])
    else:
      c=ord(sen2[i])-ord(sen1[i])
    d+=c
  for i in range(a,b):
    c=ord(sen2[i])-96
    d+=c
print(d)

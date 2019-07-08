n1,k1=input().split() 
b=input().split()
n=int(n1)
k=int(k1)
s1=[]
s2=[]
for i in b:
  s1.append(int(i))
for i in range(k):
  u1,v1=input().split()
  u=int(u1)
  v=int(v1)
  c=0
  for j in range(u-1,v):
    c=c+s1[j]
  s2.append(c)
for k in range(len(s2)):
  print(s2[k])
#

s1=[]
n=int(input())
for i in range(n):
  a=input().split()
  for j in a:
    s1.append(int(j))
s1.sort()
for i in range(len(s1)):
  print(s1[i],end=" ")

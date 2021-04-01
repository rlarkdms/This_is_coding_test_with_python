n=int(input())

d={}

for i in range(0,n):
  a,b=input().split()
  d[a]=b
dict=sorted(d.items(), key=lambda x:x[1])

for i in dict:
  print(i[0] ,end=' ')
n=int(input())

arr=[]
for i in range(n):
  k=int(input())
  arr.append(k)

arr.sort(reverse=True)

for j in arr:
  print(j, end=' ')
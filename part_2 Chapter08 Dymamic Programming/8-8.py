#효율적인 화폐의 구성.
#test
#Test2

n,m=map(int,input().split())

arr=[0]*(n)


for i in range(n):
  arr[i]=int(input())


dp=[0]*(m+1)

for i in arr:
  k=1
  val=1
  while (k*i)<(m+1):
    dp[k*i]+=val
    k+=1
    val+=1

if dp[m]==0:
  print(-1)
else:
  print(dp[m])

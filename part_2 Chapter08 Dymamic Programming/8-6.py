n=int(input())

arr=list(map(int,input().split()))

#이거 잘 생각해보자 i-1은 i-2부터 가능한거야...
point=2

#여기서 최고로 크게 할수 있는 값을 고르면 돼 잘 생각해봐....!
dp=[0]*n

dp[0]=arr[0]
dp[1]=arr[1]
while(True):

  #print(dp)
  if point>=n:
    break
  if dp[point]==0:
    #0,i-2중에 가장 큰 값을 고르며 되는거임.
    dp[point]=arr[point]+max(dp[0:point-1])
    point+=1
  

print(max(dp))


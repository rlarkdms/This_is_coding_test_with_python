# 1로 만들기 
# 진짜 예전에 풀는거 도전했다 실패한 문제인데 한번 풀어보자

#x가 5로 나누어 떨어지면, 5로 나눈다.
#x가 3으로 나누어 떨어지면, 3으로 나눈다.
#x가 2로 나누어 떨어지면, 2로 나눈다.
#x에서 1을 뺸다.
#1를 만들려고 할때 사용하는 횟수의 최솟값

d=[-1]*30000

n=int(input())
d[1]=0
d[2]=1
d[3]=1
d[4]=2
d[5]=1

a=0
for i in range(6,n+1): #생각해보니 가장 적은걸 고르면 되잖아
  min_val=9999999
  if i%5==0:
    a=int(i/5)
    if min_val>=d[a]:
      min_val=d[a]
    a=0
  if i%3==0:
    a=int(i/3)
    if min_val>=d[a]:
      min_val=d[a]
    a=0
  if i%2==0:
    a=int(i/2)
    if min_val>=d[a]:
      min_val=d[a]
    a=0
  
  a=i-1
  if min_val>=d[a]:
    min_val=d[a]
  
  d[i]=d[a]+1
print(d[n])



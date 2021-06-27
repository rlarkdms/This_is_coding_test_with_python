
x=int(input())

d=[0] *30001

for i in range(2,x+1):
  d[i]=d[i-1]+1 #비교군을 두고서 하나하나 다 비교해서 가장 작은걸 고르는거구나...
  if i%2==0:
    d[i]=min(d[i],d[i//2]+1)
  if i%3==0:
    d[i]=min(d[i],d[i//3]+1)
  if i%5==0:
    d[i]=min(d[i],d[i//5]+1)

print(d[x]) 
n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort(reverse=True)#데이터 내림차순 정렬
sum=0# 합을 알기 위해 sum 변수 선언
count=0# 언제 m이 다 달았는지를 알기 위해서 count변수 선언
for i in range(0,m):#m 만큼 도는데
  if k==count:
    sum=sum+data[1]#k==count같으면 두번째 값을 넣고 다시 첫번째로 토스!
    count=0
  else:
    count+=1
    sum=sum+data[0]

print(sum)
  
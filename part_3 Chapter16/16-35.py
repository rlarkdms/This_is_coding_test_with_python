#못생긴 수
# 2,3,5의 소인수를 가지는 수를 못생긴 수라고 한다.
# 1,2,3,4,5,6,8,9,10,12,15 를 못생긴 수라고 한다.

dp=[0]*1000001
n=int(input())
#딱 꼬라지 보니까 에라토스 체인가? 그 문제 처럼 나오는거마다 *2, *3, *5

dp[1]=1

for i in range(1000001//5):#이게 1000은 어느정도인지 잘 모르겠는데 최대한 큰 숫자로 잡음.
    if dp[i]==1:#만약 1일 경우
        dp[i*2]=1#*2 는 1
        dp[i*3]=1#*3 은 1
        dp[i*5]=1#*5 는 1

count=0
for k in range(len(dp)):# 값 찾기.
    if dp[k]==1:
        count+=1
    if count==n:
        print(k)
        break




# while rep: #이방법은 문제가 있네...ㅎㅎㅎ..
#     if len(dp)>n:
#         break
#     a=rep.popleft()
#     rep.append(a*2)
#     rep.append(a*3)
#     rep.append(a*5)
#     dp.append(a*2)
#     dp.append(a*3)
#     dp.append(a*5)


a,b=map(int,input().split())
#이거 그냥 k로 나눠지지 않으면 바로 1뺴고 1뺴고 하면 될것 같은데?
count=0

while a!=1: #a가 1이 아닐떄동안 돌기
  if a%b==0:#a의 값이 b로 나눠떨어질 떄에는 나누기
    a=a/b
  else:#아닐떄에는 -1을 실행.
    a=a-1
  count+=1
print(count)
#아니 근데 테스트 케이스가 너무 없어서 못쓰것는데...;;
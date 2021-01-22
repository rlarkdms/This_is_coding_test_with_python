#상하좌우
N=int(input())
arr=list(input().split())
x=1
y=1


for i in arr:
  if i =='L':#왼쪽으로 갈때
    if y==1:#왼쪽에 암것도 없으면 pass
      pass
    else:
      y=y-1
  if i =='R':
    if y==N:#오른쪽에 암것도 없으면 pass
      pass
    else:
      y=y+1
  if i =='U':
    if x==1:#위에 암것도 없을떄는 pass하고
      pass
    else:
      x=x-1
  if i =='D':
    if x==N:#아래에 암것도 없으면 pass함
      pass
    else:
      x=x+1

print("%d %d" %(x,y))
#나동빈씨도 나랑 똑같이 하긴했는데 그 분은 변수를 다 맞춰서 진행함.

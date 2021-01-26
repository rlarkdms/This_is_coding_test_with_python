a,b=map(int,input().split())
x,y,loca=map(int,input().split())

array=[list(map(int, input().split())) for _ in range(a)]
#만약 가본 곳이 면 2로 표시 하기.

current_location=[x,y]
count=0
number_location=0# 4바퀴 도는걸 표현하기 위해
# 1번 구현

direction=[[0,-1],[1,0],[0,1],[-1,0]]
#0->북
#1->동
#2->남
#3->서
array[x][y]=2

while True:
  #이 부분이 왼쪽으로 도는 부분.
  if loca==0:
    loca=3
  elif loca==1:
    loca=0
  elif loca==2:
    loca=1
  elif loca==3:
    loca=2

  local_x=direction[loca][0]+current_location[0]#이건 가야하는 좌표 표시
  local_y=direction[loca][1]+current_location[1]
#이게 왼쪽 칸임

#1번 조건 ->만약 거기가 가보지 않은 곳이면 가기
#결국 하나임 왼쪽 방향으로 회전 만약 안가본곳이면 가고 아니면 그냥 있어
  if array[local_x][local_y]==0:#만약 거기 안에 좌표가 안가본 곳이면 간다.
    current_location[0]=local_x
    current_location[1]=local_y
    array[local_x][local_y]=2
    print(local_x)
    print(local_y)
    number_location=0# 좌표가 움직이면 도는 바퀴는 0으로 set되어야 함.
  else:#아니면 
    number_location+=1 # 도는 바퀴 추가
    if number_location==4:
     
      if loca==0:
        loca=2
      elif loca==1:
        loca=3
      elif loca==2:
        loca=0
      elif loca==3:
        loca=1

      local_x=direction[loca][0]+current_location[0]
      local_y=direction[loca][1]+current_location[1]
      number_location=0# 좌표가 움직이면 도는 바퀴는 0으로 set되어야 함.
      if array[local_x][local_y]==1:
        break
print(array)
for i in range(len(array)):# 그중에 2의 값 찾기.
  for j in range(len(array[0])):
    if array[i][j]==2:
      count+=1

print(count)
#흠 테스트케이스를 찾고 싶은데....일단 이렇게 하면 되긴함. 간단한 케이스에서는 다 통과됨... 흠 테스트 케이스 구하고 싶다.
#미로 탈출
#BFS는 너무 어렵다....이거는 그냥 예제를 카피하자 나는야 카피캣

from collections import deque
#이거 모듈

n,m=map(int,input().split())

graph=[]

for i in range(n):
  graph.append(list(map(int,input().split())))

#여기까지는 입력단.

dx=[-1,1,0,0]
dy=[0,0,-1,1]
#dx,dy는 그냥 위치를 나타내기 위함임..!


def BFS(x,y): 
  queue=deque()
  queue.append((x,y))
  
  while queue:# 와 이거 큐 문제때문에 넣는거였구나.
    x,y=queue.popleft()

    for i in range(4):
      nx=x+dx[i]#그위치에서 위아래오흔쪽 왼쪽을
      ny=y+dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=m:#범위를 넘어가면 
        continue
      if graph[nx][ny]==0: #그부분이 괴물이 있는곳이면 넘어가기.
        continue
      if graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1#이게 그 원래 값에 +1 와 맞다 이렇게하면 되네
        queue.append((nx,ny))#그 부분 큐에 넣고 
  return graph[n-1][m-1]# 그위치 값.

print(BFS(0,0))

#방문원이 있는데 이 방문원이 어떤 장소 K(소개팅 장소)를 경유하여 X(회사)까지 가는 최소시간을 출력해라
# 일단 노드간의 거리는 무조건 1로 설정.
#입력값은 첫번째 줄의 두 값은 회사의 개수N, 경로의 개수 M
# 두번째 줄 부터 M+1번째 줄까지는 노드간의 연결
# M+2 번째 줄에는 X와 K가 주어진다.

#이 문제는 다익스트라 플로이드 워셜 둘다 가능하다 이유는 
# 다익스트라의 경우에는 1부터 K까지의 최단경로를 구하고 K 부터 X까지의 최간 경로를 구해서 더하면 되니까
# 또한 플로이드 워셜의 경우에는 특정 노드에서 특정노드까지의 경로 구하기가 다 가능하다.
# 그런데 이 문제의 경우에는 플로이드 워셜을 사용하는것이 좋다.
#책에서도 그렇게 나왔있기도 하고 범위가 적기 때문에 복잡도가 큰 플로이드워셜을 쓰는게 적합해보인다.

INF=int(987654321)

n,m=map(int,input().split())

graph=[[INF]*(n+1) for _ in range(n+1)]


for i in range(1,n+1): #여기 중간은 값을 0으로 설정
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0
#위에 부분은 위가 아니라
#아래같이 해도 상관없지 않을까? 위로 하면 두번을 돌아야하니까 depth에 안좋을것 같은 느낌?
# for i in range(1,n+1):
#   graph[i][i]=0



for i in range(m):
  a,b=map(int,input().split())
  graph[a][b]=1#경로값은 무조건 1이라서 이렇게 설정.
  graph[b][a]=1#와 이거 하나때문에 계속 돌았네... 하....#여기 전제 조건중에 노드가 연결되어있다면 왔다갔다 할 수 있다라는 조건떄문에 방향성이 생기지 않고 와리가리로 1를 정의해야한다.



for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])#다 돌면서 거리값 정의
      #graph[b][a]=min(graph[b][a],graph[b][k]+graph[k][a])

X_com,K_com=map(int,input().split())
#K를 들렸다 X로 가야하는 거임.

for i in graph:
  print(i)
#print(graph)
if (graph[1][K_com]+graph[K_com][X_com])>=INF:#1->K간거랑 k->X간거 더해서 값 정의 / 그값중에 무한 이 포함되어 있으면 -1로 정의
  print(-1)
else:
  print(graph[1][K_com]+graph[K_com][X_com])

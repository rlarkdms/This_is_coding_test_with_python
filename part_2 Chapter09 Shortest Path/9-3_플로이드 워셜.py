INF=int(1e9)#무한을 위해
#플로이드 워셜 알고리즘 이건 쫌 이해가 가네 ㅎㅎ..
n=int(input())#
m=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]#그래프 정의

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0 #그래프 중간은 0으로 정의 이유가 자기 자신은 초기화하기 위해서



for _ in range(m):
  a,b,c=map(int,input().split())# a는 노드 b는 그 뒤에 노드 C는 거리값 
  graph[a][b]=c#a b 다음에 거리값 정의

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])#이게 돌면서 1~돌면서 거리값이 작은게 있으면 갱신하는 식으로 설정.
      #Dab=min(Dab,Dak+Dkb) 이런 점화식으로 설정.

for a in range(1,n+1): #결과값 출력
  for b in range(1,n+1):
    if graph[a][b]==INF:
      print("INFINITY", end=" ")
    else:
      print(graph[a][b], end=" ")

  print()


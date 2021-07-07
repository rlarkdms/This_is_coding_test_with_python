import sys
input=sys.stdin.readline
INF=int(1e9) #INF=987654321 도 가능

n,m=map(int,input().split())

start=int(input())
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)#방문 했는지 아닌지
distance=[INF]*(n+1)# 최단 거리 리스트

for _ in range(m):
  a,b,c=map(int,input().split())
  #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
  graph[a].append((b,c))

def get_smallest_node():#가장 짧은 거리를 갱신하는 함수.
  min_value=INF
  index=0 #가장 최단 거리가 짧은 노드(인덱스)
  for i in range(1,n+1):
    if distance[i]<min_value and not visited[i]:#갱신된게 더 작을 때 
      min_value=distance[i]#바꾸는 거
      index=i
  return index

def dijkstra(start): #다익스트라 알고리즘
  distance[start]=0#처음 시작
  visited[start]=True#여기가 True인 이유는 방문을 해서 True가 된거임.
  for j in graph[start]:
    distance[j[0]]=j[1]#graph의 뒷노드가 j[0]이고 j[1]는 거리임. 그래서 j[0]은 j[1]의 거리인거임.
  
  for i in range(n-1):#노드 수 -1  #사실 이해가 잘 안가네....흙흙 머리가 안좋아서 그런가...?
    now=get_smallest_node()#그림은 이해가 갔는데;;
    visited[now]=True
    for j in graph[now]:
      cost=distance[now]+j[1]
      if cost<distance[j[0]]:
        distance[j[0]]=cost

dijkstra(start)

for i in range(1,n+1):
  if distance[i]==INF:
    print("INFINITY")
  else:
    print(distance[i])

#이게 start에서 특정 노드까지 구하는 방법
#근데 생각해보니까 그럼 플로이드 워셜 알고리즘을 쓰는게 더 나은거 아니야??
#0부터 특정 노드로 구하면 되는거잖아...? 아닌가?


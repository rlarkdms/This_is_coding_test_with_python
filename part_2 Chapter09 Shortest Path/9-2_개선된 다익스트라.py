#그냥 다익스트라는 이해를 못하겠으니까 개선된 다익스트라 알고리즘을 이해해보자
import heapq#힙 import
import sys
input=sys.stdin.readline
INF=int(1e9)#987654321도 가능

n,m=map(int,input().split())

start=int(input())

graph=[[]for i in range(n+1)] #그 다음에 올 값을 담기위해서 설정.

distance=[INF]*(n+1) # distance는 최단 경로값을 받기 위해 존재.

for _ in range(m): # a,b,c는 a는 노드 b는 a노드와 이어질 노드 c는 경로값을 의미한다.
  a,b,c=map(int,input().split())
  graph[a].append((b,c))# 그래서 그래프에다가 (이어질 노드,경로값) 순으로 삽입한다.

def dijkstra(start):# 다익스트라
  q=[]
  heapq.heappush(q,(0,start))#q에다가 힙을 push 한다는 의미이다.(경로값, 시작값)
  distance[start]=0 
  while q: #q 스택을 돌면서 
    dist,now=heapq.heappop(q) #q안에 있는 힙의 값을 빼내는데....!
    if distance[now]<dist:#이게 거리값이 적은 순서대로 빠지는 건데
      continue#여기가 이해가 안되는데....책에서는 현재 노드가 이미 처리된 적이 있는 노드라면 무시.
    for i in graph[now]:#현재 노드와 연결된 노드의 값들을 탐색하는건데. 
      cost=dist+i[1]#거리를 더하고 
      if cost<distance[i[0]]:#저장된 거리값과 현재 계산된 거리값을 비교해서 
        distance[i[0]]=cost#저장된 거리값이 더 크면 계산된 거리값을 덮어씌어서 가져가고 
        heapq.heappush(q,(cost,i[0])) #그 값은 다시 저장한다.(거리값,노드)로 저장한다.
        #아 반대인가? i[0]은 노드고 i[1]은 거리구나.

dijkstra(start)

for i in range(1,n+1):
  if distance[i]==INF:
    print("INFINITY")
  else:
    print(distance[i])

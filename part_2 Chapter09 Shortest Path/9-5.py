#전보
#어떤 나라에는 N개의 도시가 있음 
#그리고 X나라에서 Y나라까지 전보를 보내려면 X에서 Y까지 통로가 설치되어있어야 함.
# !!!중요한게 X->Y까지의 통로가 설치되어있으면 X에서 메시지 보낸게 Y에 전달 가능하지만
# Y->X의 통로가 없다면 Y에서 X까지의 메시지 전달이 안됨.
#메시지는 일정 시간이 필요하다==거리값이라는 얘기

#위까지는 전제 조건이고 문제는 C라는 나라에서 위급사황이라 최대한 많은 나라에 메시지를 보내려고 함.
#그럴 때 메시지를 보낼 수 있는 나라는 몇개이며, 모두가 메시지를 전달 받았을때 얼마큼의 시간이 걸리는가를 측정하는 문제이다.


#일단 이문제는 플로이드로 풀 수 없음 이유는 범위가 너무 커서 시간 복잡도가 너무 커짐.abs
#최대 30000*30000*30000인 27,000,000,000,000이라는 연산속도가 걸림 안됨.
#그래서 이문제는 무조건 다익스트라 알고리즘을 이용해야함.

#일단 첫번째 줄에 도시의 개수(N) 통로의 개수(M) 메시지를 보내고자하는 도시(C)가 주어진다.
#두번째 줄부터 M+1까지는 통로 노드 첫번째 노드 두번째 그리고 거리값이 주어진다.

#이 문제의 포인트는 최단 거리로 갈 수 있는 곳 중에 가장 오래걸리는 곳을 찾아내는 것임.


import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m,start=map(int,input().split())

graph=[[] for _ in range(n+1)]

distance=[INF]*(n+1)


for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))#  그래프 뒤에 올 원소같은거 넣기



def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))


dijkstra(start)
count_val=0
for i in range(1,len(distance)):
  if distance[i]>0:
    count_val+=1

print("%d %d" %(count_val,max(distance[1:])))


#Python 처럼 짠다는건 이렇게 짜는게 아닌듯
#아래가 챗에 나온 부분인데 이렇게 짜야하나보다...

# count=0
# max_distance=0

# for d in distance:
#   if d!=INF:
#     count+=1
#     max_distance=max(max_distance,d)#흠 큰값고르기 할때 이 포멧이 좋겠구만...

# print(count-1,max_distance)






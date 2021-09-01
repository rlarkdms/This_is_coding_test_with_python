#플로이드
#n개의 도시가 있다. 한 도시에서 출발하여 다른 도시에 도착하는 버스가 있다.
#한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스가 있다.
#각 버스는 한번 사용할 때 필요한 비용이 있다.

#요구사항 : 도시 A->B가는 최소 비용을 구해라....!

#그냥 플로워셜 알고리즘....
#엥? 이게 시간초과라고?
#도대체 시간 초과가 어디에서 나는거야...? -> sys.stdin.readline()이 문제였다.
import sys
n=int(input())
m=int(input())

graph=[[987654321]*(n+1) for _ in range(n+1)]#그래프 정의

for i in range(1,n+1):#0으로 셋
    graph[i][i]=0

for i in range(m):#간선 컴온
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a][b]=min(graph[a][b],c)


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==987654321:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

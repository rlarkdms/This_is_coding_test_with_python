def DFS(graph,v,visted):#그래프,위치,방문노드
  visted[v]=True
  print(v)
  for i in graph[v]:
    if not visted[i]:
      DFS(graph,i,visted)

graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]


visted=[False]*9
DFS(graph,1,visted)
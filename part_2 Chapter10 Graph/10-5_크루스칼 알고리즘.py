def find_parent(parent,x):#부모 노드를 찾는 과정.
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):#유니온 이게 더작은 값으로 정의하는 것.
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

edges=[]
result=0

for i in range(1,v+1):#parent 정의를 하고
  parent[i]=i

for _ in range(e):# 비용과 간선들 정보를 얻기.
  a,b,cost=map(int,input().split())
  edges.append((cost,a,b))

edges.sort()#작은 순서대로 정렬

for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):#이게 순환이 아니면 이란 뜻.
    union_parent(parent,a,b)
    result+=cost#최소 비용 합하기

print(result)

#음 이건 이해가 쫌 간다.
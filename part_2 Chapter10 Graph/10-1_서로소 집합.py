#아니 근데 궁금한게 서로소는 어디에 필요한거지?? 알 수가 없는데;;
#어떤 문제를 풀 때 필요할까???음..알 수가 없는데;;

def find_parent(parent, x):#부모 노드를 찾는거 부모는 노드는 자식노드보다 무조건 큼.
  if parent[x]!=x:
    return find_parent(parent, parent[x])
  return x

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

v,e=map(int,input().split())#노드(node) 개수랑 간선(edge) 개수
parent=[0]*(v+1)#부모 노드를 알기 위해서 하는 것.

for i in range(1,v+1):# 테이블 초기화
  parent[i]=i

for i in range(e):
  a,b=map(int,input().split())#값 받고 돌리기.
  union_parent(parent,a,b)

print('각 원소가 속한 집합: ' , end='')

for i in range(1,v+1):
  print(find_parent(parent,i), end=' ')

print()

print('부모 테이블: ', end='')
for i in range(1,v+1):
  print(parent[i], end=' ')

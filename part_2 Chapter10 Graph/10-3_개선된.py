def find_parent(parent, x):#부모 노드를 찾는거 부모는 노드는 자식노드보다 무조건 큼.
  if parent[x]!=x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

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


# 서로소 집합 알고리즘이랑 개선된 서로소 집합 알고리즘이랑 다른 점이 있다.
# 부모테이블 노드가 다르다. 경로압축 방법...?
# 이해는 안가니까 포맷을 외워두자 개선된 서로소가 더 사용하기 편하기도 하고 좋다. 

# 팀 결성.
# 학교에서 0~N 까지의 번호를 부여했다.
# 팀 합치기 연산 -> 두 팀을 합치는 연산.
# 같은 팀 여부 확인 연산 두 학생이 같은 팀에 속하는지 확인하는 연산.abs
# 이 문제 아까 계속 했던 서로소 문제다.

# N은 번호 M은 연산의 개수 
# 0 a b 는 팀 합치기 연산
# 0 a b는 같은 팀 여부 확인 연산

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
  a,b,c=map(int,input().split())#값 받고 돌리기.
  if a==0:
    union_parent(parent,b,c)
  elif a==1:
    if parent[b]==parent[c]:
      #이게 책상에는 
      # if find_parent(parent,a)==find_parent(parent,b): 로 되어있음.
      # 그런데 개선된 서롯소 집합 알고리즘이라서 그냥 parent 리스트의 값만 확인해보면 될 것 같은데?
      print('YES')
    else:
      print('NO')
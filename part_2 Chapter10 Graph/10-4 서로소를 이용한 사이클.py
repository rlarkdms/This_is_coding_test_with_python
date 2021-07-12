def find_parent(parent, x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
  parent[i]=i

cycle=False

for i in range(e):
  a,b=map(int,input().split())
  if find_parent(parent,a) ==find_parent(parent,b):#이게 사이클이 생기면 이란 뜻인데.
    #a,b가 같은 곳을 가르킨다는것(부모가 같다는것)은 사이클이 있다는 얘기니 cycle=True
    cycle=True
    break
  else:
    union_parent(parent,a,b)
if cycle:
  print("사이클이 발생했습니다")
else:
  print("사이클이 발생하지 않았습니다.")

#감을 못잡겠다 이게 왜 있는지 모르겠음.

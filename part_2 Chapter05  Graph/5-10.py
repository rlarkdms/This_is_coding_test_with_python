a,b=map(int,input().split())

graph=[]
for i in range(a):
<<<<<<< HEAD
  graph.append(list(map(int,input().split())))
  
result=0
#깊이 우선임 그래서 지나간곳은 1로 바꾸고 그 있던곳은 +1 시키면 됨.

def dfs(x,y):
  if x<=-1 or x>=a or y<=-1 or y>=b:
    return False

  if graph[x][y]==0:
    graph[x][y]=1#이렇게해야 연쇄적으로 그 주변 값들이 다 바뀜.
    dfs(x,y-1)
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y+1)
    return True# 이게 0이면 무조건 True 주고 재귀 호출로 주변 값을 다 1로 바꾸는 거임.
  return False #False인 이유는 지금 아무것도 거치지 않았기 때문에 False임.
  


for i in range(a):
  for j in range(b):
    if dfs(i,j)==True:#배열 돌아다니면서 함수 호출한게 0일시에는 result+=1
      result+=1


print(result)
=======
  graph.append(list(map(int,input())))

visted=[False]*(a*b)

>>>>>>> 5de648917941d08b7a95fbf6fe79576f03b91d48

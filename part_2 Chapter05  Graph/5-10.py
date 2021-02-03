a,b=map(int,input().split())

graph=[]
for i in range(a):
  graph.append(list(map(int,input())))

visted=[False]*(a*b)


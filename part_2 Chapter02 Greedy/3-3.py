a,b=map(int,input().split())

down=0

for i in range(0,a):
  arr=list(map(int,input().split()))
  if down<min(arr):
    down=min(arr)

print(down)
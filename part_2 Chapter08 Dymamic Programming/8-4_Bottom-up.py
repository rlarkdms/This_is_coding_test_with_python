d = [0]*100

d[1]=0
d[2]=0

for i in range(3,100):
  d[i]=d[i-1]+d[i-2]

n=int(input())
print(d[n])


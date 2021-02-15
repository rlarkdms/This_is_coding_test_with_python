#볼링공 고르기 문제...!
import itertools

a,b=map(int,input().split())

arr=list(map(int,input().split()))

count=0

result =list(itertools.combinations(arr,2))

for i in result:
  if i[0]!=i[1]:
    count+=1

print(count)
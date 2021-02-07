n=int(input())

arr=list(map(int,input().split()))

#아니 최솟값도 아니고 최댓값인데...
#최댓값이 나올려면 일단 정렬을 하고 
result=0
stand=0
plus=0

arr.sort(reverse=True)

#생각해보니까 예외사항이 있다..... 내일 다시 해보자
#5 5 5 5 4  4 3 3 3 3  1

while True:
  if stand==len(arr):
    break
  if stand>len(arr):
    result-=1
    break
  result+=1
  stand = stand + arr[stand]

print(result)
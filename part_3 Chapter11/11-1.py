n=int(input())

arr=list(map(int,input().split()))

#최댓값이 나올려면 일단 정렬을 하고 
result=0
stand=0

arr.sort()

#생각해보니까 예외사항이 있다..... 내일 다시 해보자
#5 5 5 5 4  4 3 3 3 3  1->o
#1  3 3 3  3->O
#1 2 2 2 3 ->O
# 2 2 2 2 2->X
# 1 1 3 3 3->O


for i in arr:
  stand+=1
  if i==stand:#풀이랑 다른건 이거 하나 다른데 ==이면 되지 않나?
    result+=1
    stand=0

print(result)

#이 방법은 예외사항 처리 못하는게 존재함....
# while True:

#   if stand>=len(arr):
#     break

#   stand = stand + arr[stand]
#   result+=1
  
# print(result)
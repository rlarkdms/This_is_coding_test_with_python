#만들수 없는 금액
#이거는 99.9% 런타임 에러나니까 다음번에 이 문제를 도전해본다면 풀어보고 그때도 이러면 답지 보기.
import itertools

a=int(input())


arr=list(map(int,input().split()))

result=[]

sum_each=[]


sum_all=sum(arr)#가장 크게 나올 나올수 있는 값 
for i in range(1,a+1):#조합으로 다 구해보기 내 예상 이거 테스트 케이스 있었으면 런타임 에러 떴다.... 이거 해결해야함...
  result =result+list(itertools.combinations(arr,i))

for j in result:#나온값들을 다 더해버리기...
  sum_each.append(sum(j))

sum_each.sort()

sum_set=set(sum_each)
sum_list=list(sum_set)#중복 다 없애기

for i in range(1,sum_all):
  if i not in sum_list:#순서대로 가다가 없는 숫자 나오면 print
    print(i)
    break
else:#만약 끝까지 가면 +1하기...
  print(sum_all+1)
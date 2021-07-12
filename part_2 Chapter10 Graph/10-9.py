#커리큘럼 문제

# 동빈이는 온라인으로 컴퓨터 공학 강의를 듣고 있어요.
# 선수강의를 들어야 그 다음 강의로 넘어갈 수 있다.

#강의 시간은 주어지고 순서가 주어진다 이럴 결루 걸리는 최소 시간을 구하여라

# N은 강의의 수 
# n개의 줄에는 각 강의의 시간 번호가 자연수로 주어지며, 공백 다음에는 그 강의를 듣기위해 선수강해야하는 강의
# 그 다음으로는 -1이 나온다 이때 각 줄 마다 걸리는 시간에 대해서 출력하여라.
# 이문제 어렵다....


#위상정렬의 관련해서는 절대로 순환성이 없어야함.

#import sys
from collections import deque
#input=sys.stdin.readlines
import copy

n=int(input())

cost=[0]*(n+1) #강의의 비용을 넣기 위해서 존재

graph=[[] for _ in range(n+1)]

indegree=[0]*(n+1)

for i in range(1,n+1):
  result=[]
  a=list(map(int,input().split()))
  for k in range(1,len(a)-1): #선수강 해야하는 것들이고 리스트에 들어가야 할 것은 
    graph[a[k]].append(i)
    indegree[i]+=1
  
  cost[i]=a[0] #비용이고 이걸 어딘가에 저장시켜야함.

q=deque()
result=copy.deepcopy(cost)#책과 내코드랑 다른곳이 여기랑 
#여기는 이해가 감 cost의 값을 계속 가지고 있어야 하기 때문에 copy.deepcopy(cost)라고 한게 맞고 

for i in range(1,n+1):
  if indegree[i]==0:
    q.append(i)

while q:
  now=q.popleft()
  result.append(now)


  for i in graph[now]:
    print("result[i]]의 값: %d" %result[i])
    print("result[now]+cost[i]의 값 %d" %(result[now]+cost[i]))
    result[i]=max(result[i],result[now]+cost[i])#여기 부분 두군데 임.
    indegree[i]-=1
    if indegree[i]==0:
      q.append(i)

for i in range(1,n+1):
  print(result[i])




#포기! 어떻게 하든 같은 값밖에 나오지 않음. 해결 불가능.
# 문제 솔직히 이해가 너무 안된다. 특히 라인 54번째가 왜 저렇게 진행하는지 값이 안잡힌다.
# 이전까지의 값 더하기 cost[i] 가 더 크면 result[i]인것 같은데 음... 도저히 이해가 안된다.
# 이럴때는 넘어가고 다음에 다시 보자

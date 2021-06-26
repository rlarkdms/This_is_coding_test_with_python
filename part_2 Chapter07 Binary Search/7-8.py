#일단 떡볶이집 이 문제는 인강들었을 때 결정알고리즘 문제로 많이 나왔던 유형이야....!
#결정 알고리즘을 풀 때는 파라메트릭 서치
def bin(start,end,target,arr):
  sum_value=0
  while start<=end:
    sum_value=0
    mid=(start+end)//2
    for i in arr:
      if (i-mid)>0:
        sum_value+=(i-mid)   
    if sum_value==target:
      return mid
    elif sum_value>target:
      start=mid+1
    elif sum_value<target:
      end=mid-1
  return None


n,m=map(int,input().split())

arr=list(map(int,input().split()))

print(bin(0,max(arr),m,arr))


#계수 정렬로 풀기. 굉장히 간단하게 풀수 있음!

n=int(input())
arrA=list(map(int,input().split()))
m=int(input())
arrB=list(map(int,input().split()))

arr_ori=[0]*1000001

for i in arrA:
  arr_ori[i]=1

for i in arrB:
  if arr_ori[i]==1:
    print("yes", end=' ')
  if arr_ori[i]==0:
    print("no", end=' ')


    


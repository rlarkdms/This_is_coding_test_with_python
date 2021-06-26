#이진 탐색으로 문제 풀기.

def bin(first,last,val,arr):#이 포맷을 그냥 기억하고 있기 중요함.
  while first<=last:
    mid=(first+last)//2
    if arr[mid]==val:
      return arr[mid]
    elif arr[mid]>val:
      last=mid-1
    elif arr[mid]<val:
      first=mid+1
  return -1

n=int(input())
arrA=list(map(int,input().split()))

m=int(input())
arrB=list(map(int,input().split()))

arrA.sort()#? 뭐야 이거 되는 문법이였어?

for i in arrB:

  if bin(0,n-1,i,arrA)==-1:
    print('No', end=' ')
  else:
    print('Yes', end=' ')

#집합 자료형으로 풀기

n=int(input())
arrA=set(map(int,input().split()))#그니까 A는 중복될 수 있어서 이렇게 진행하는 거구나...!

m=int(input())
arrB=list(map(int,input().split()))

for i in arrB:
  if i not in arrA:
    print("no", end=' ')
  else:
    print("yes", end=' ')
    break # 있으면 바로 나가기 계속 돌면 실행 속도를 너무 잡아먹음.


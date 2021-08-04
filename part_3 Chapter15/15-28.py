# 고정점 찾기
# 인덱스 값이랑 value랑 같은 위치 찾기 최대 1개의 고정점이 있음
# 고정점이 없다면 -1를 출력하기.
# 시간복잡도가 O(logN)이여야 하고
# 1 <= N <= 1,000,000
import sys

N=int(input())
arr=list(map(int,sys.stdin.readline().split()))
start=0
last=N-1

while True:# 이문제는 이분탐색으로 돌다가 만약 mid가 arr[mid]보다 크면 오른쪽으로 작은면 왼쪽으로 탐색하는 걸 만들기만하면 됨.
    mid=(start+last)//2
    if mid==arr[mid]:#고정점이 있을 때 하나라도 하니까 무조건 하나 생기면 멈춰버리기.
        print(mid)
        break
    if start>=last:#만약 아무런 값이 없을 경우
        print(-1)
        break

    if mid>arr[mid]:
        start=mid+1
    elif mid<arr[mid]:
        last=mid-1
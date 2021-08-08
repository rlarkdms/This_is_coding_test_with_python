#금광 문제
#n*m 크기의 금광이 있고
#이 문제 전형적인 DP 문제

T=int(input())#테스트 케이스 받기.
max_arr=[]
for i in range(T):

    n,m=map(int,input().split())
    arr = []
    arr=list(map(int,input().split()))
    arr_sort=[[] for i in range(n)]

    for j in range(len(arr)):
        arr_sort[j//m].append(arr[j])

    for a in range(1,m):
        for b in range(n):
            if b==0:#만약 맨 위면 왼쪽이나 왼쪽 아래꺼만 고를 수 있어서 이렇게 정함
                if arr_sort[b][a-1]>arr_sort[b+1][a-1]:
                    arr_sort[b][a]+=arr_sort[b][a-1]
                else:
                    arr_sort[b][a]+=arr_sort[b+1][a-1]
            elif b==n-1:#만약 맨 아래면 왼쪽이나 왼쪽 위꺼만 고를 수 있어서 이렇게 정함
                if arr_sort[b][a-1]>arr_sort[b-1][a-1]:
                    arr_sort[b][a]+=arr_sort[b][a-1]
                else:
                    arr_sort[b][a]+=arr_sort[b-1][a-1]
            else:#중간이면 왼쪽 왼쪽 위 왼쪽 아래 중에 골라서 더하기.
                if arr_sort[b][a-1]>=arr_sort[b-1][a-1] and arr_sort[b][a-1]>=arr_sort[b+1][a-1]:
                    arr_sort[b][a] += arr_sort[b][a-1]
                elif arr_sort[b-1][a-1]>=arr_sort[b][a-1] and arr_sort[b-1][a-1]>=arr_sort[b+1][a-1]:
                    arr_sort[b][a] += arr_sort[b-1][a-1]
                elif arr_sort[b+1][a-1]>=arr_sort[b][a-1] and arr_sort[b+1][a-1]>=arr_sort[b-1][a-1]:
                    arr_sort[b][a] += arr_sort[b+1][a-1]
    max_value=0
    for k in range(n):#맨 마지막 행중에 가장 큰 값을 max_arr에 append
        if arr_sort[k][m-1]>=max_value:
            max_value=arr_sort[k][m-1]

    max_arr.append(max_value)

for i in max_arr:
    print(i)

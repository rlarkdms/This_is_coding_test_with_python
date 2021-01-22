n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort(reverse=True)#데이터 내림차순 정렬

#책에서 원하는건 간단한 풀이 그래서
val=m//(k+1)
print((data[0]*k+data[1])*val+data[0]*(m%(k+1)))
#만약 2 4 5 4 6이 있다고 할때
# k의값이 3 이라면
# 6 6 6 5 6 6 6 5 이런식으로 갈것 이다.
#이러면 while문이나 for문을 돌리지 말고 간단하게 계산식으로 알고리즘을 풀라는 말
#그냥 더하기로 해결해라ㅎㅎㅎㅎㅎ
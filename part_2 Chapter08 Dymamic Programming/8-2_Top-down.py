d= [0]*100

def fibo(x):
  if x==1 or x==2:#1,2의 값은 이미 정해져있고
    return 1
  if d[x]!=0:# 만약 계산이 되어있는 거면 그냥 return 이고
    return d[x]

  d[x]=fibo(x-1) +fibo(x-2) #계산이 안되어있는 거면 d[x]를 계산하기
  return d[x]# 리턴
print(fibo(99))


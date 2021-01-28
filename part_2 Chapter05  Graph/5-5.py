#팩토리얼 재귀함수로 구현
def re_function(i):
  if i==1:
    return 1

  return i*re_function(i-1)
  

print(re_function(5))
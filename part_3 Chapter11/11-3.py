#문자열 뒤집기...!

#일단 숫자가 다 같으면 돌 필요가 없음
#문제는 100만까지의 단위가 있음 이걸 해결하기 위해서는 for문을 한번만 돌아야함....! 어차피 메모리는 많이 써도 상관없음.

number=input()

number=list(number)
result1=0
result2=0

if number[0]=='1':
  result1+=1
if number[0]=='0':
  result2+=1

for i in range(1,len(number)):
  if number[i-1]=='0' and number[i]=='1':
    result1+=1
  if number[i-1]=='1' and number[i]=='0':
    result2+=1


if result1<=result2:
   print(result1)
else:
   print(result2)
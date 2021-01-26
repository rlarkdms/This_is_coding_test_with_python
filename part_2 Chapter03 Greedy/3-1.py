money=int(input("입력값:"))

array=[500,100,50,10]
count=0

for i in array:
  count=count+money//i
  money=money%i

print(count)


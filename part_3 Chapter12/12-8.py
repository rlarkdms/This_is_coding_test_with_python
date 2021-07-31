#문자열 재정렬
string=input()

alp=[]
num=[]
sum_all=0
all=""

for i in string:
  if i.isalpha():
    alp.append(i)

  if i.isdigit():
    num.append(int(i))

alp.sort()
sum_all=sum(num)


for i in alp:
  all=all+i

print(all+str(sum_all))
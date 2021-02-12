number=input()


#보통은 곱하기가 더 큰수를 가져온다는건 알고있는 사실임 더하기를 쓰면 좋을떄가 언제인지를 파악하면됨.
#일단 숫자중에 0이 들어갈때임. 그 상황 빼고는 다 곱하기...!
#--------------------아 답지 찾아보니까 1일 상황에서도 더하기이다!

number=list(number)
result=1
if number[0]==1:
  number.insert(0,number[0]+number[1])
  del number[1]
  del number[1]
if number[len(number)-1]==1:
  number.append(number[len(number)-1]+number[len(number)-2])

#1은 보니까 앞뒤 비교해서 작은 숫자랑 더해야함.
#for i in range(1,len(number)-1):
#  if i=='1':
#    if number[i-1]>number[i+1]

#      number[i-1]+number[i]

#  else:
#    array=array+number[i]


#else:
#  if i!='0':
#    result=result*int(i)    
print(number)

print(result)
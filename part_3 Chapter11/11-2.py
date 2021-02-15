number=input()


#보통은 곱하기가 더 큰수를 가져온다는건 알고있는 사실임 더하기를 쓰면 좋을떄가 언제인지를 파악하면됨.
#일단 숫자중에 0이 들어갈때임. 그 상황 빼고는 다 곱하기...!
#--------------------아 답지 찾아보니까 1일 상황에서도 더하기이다!
#이거에서 더 간단하게 할 방법을 찾아보자

number=list(number)
result=1
i=1

while True:
  if number[0]=='1' and len(number)==1:
    break
  
  if '1' not in number:
    break 


  if '1' in number:


    if number[0]=='1':
      number.insert(0,str(int(number[0])+int(number[1])))
      del number[1]
      del number[1]
    if number[len(number)-1]=='1':
      number.append(str(int(number[len(number)-1])+int(number[len(number)-2])))
      del number[len(number)-2]
      del number[len(number)-2]
    
    if '1' not in number:
      break 

#1은 보니까 앞뒤 비교해서 작은 숫자랑 더해야함.
    while True:
      if i==len(number)-1:
        break
      if number[i]=='1':
        if number[i-1]<=number[i+1]:
          number.insert(i,str(int(number[i])+int(number[i-1])))
          del number[i+1]
          del number[i-1]
          i=-1
        else:
          number.insert(i,str(int(number[i])+int(number[i+1])))
          del number[i+1]
          del number[i+1]
          i-=1
      i+=1

for i in number:
  if i!='0':
    result=result*int(i)
  if number[0]=='0' and len(number)==1:
    result=0 

print(result)
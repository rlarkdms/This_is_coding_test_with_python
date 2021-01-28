t=int(input())


count=0

for i in range(0,t+1):
  for j in range(0,60):
    for k in range(0,60):
      if str(str(i)+str(j)+str(k)).find("3")!=-1:
        count+=1

print(count)
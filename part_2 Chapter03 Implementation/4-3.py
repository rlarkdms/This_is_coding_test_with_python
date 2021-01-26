aa=input()

# this exam should know number of cases
# example right 2, up 1 / right 2 down 1 
# left 2 up 1 /left 2 down 1
# up 2 right 1/ up 2 left 1
# down 2 right 1 /down 2 left 1
a1=ord(aa[0])-96
b1=int(aa[1])

count=0

array=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

for i in array:
  if ((i[0]+a1>=1)and(i[1]+b1>=1))and((i[0]+a1<=8)and(i[1]+b1<=8)):
    count+=1
print(count)
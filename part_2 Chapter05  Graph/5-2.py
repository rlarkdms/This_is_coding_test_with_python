que=[]

que.append(5)# 5
que.append(2)# 5 2
que.append(3)# 5 2 3
que.append(7)# 5 2 3 7
que.popleft() #이게 큐에서 pop나오는거# 2 3 7
que.append(1)# 2 3 7 1
que.append(4)# 2 3 7 1 4
que.popleft() #이게 큐에서 나오는거 # 3 7 1 4

print(que)
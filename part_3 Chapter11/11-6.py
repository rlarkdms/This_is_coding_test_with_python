#음식이 있고 회전판에 먹어야할 음식 N개가 있음.
#잠만 그럼 food_times이라고 보는 배열에서 먹고 그냥 끝내는거 아니야?
#food_times=[4,2,3,6,7,1,5,8] k=16 answer = 3
#food_times=[4,2,3,6,7,1,5,8] k=27 answer = 5
#안 맞는 케이스가 있음 찾아봐서 코드 고치기.
#효율성의 문제있음...정확성은 다 통과함.
food_times=list(map(int,input().split()))
k=int(input())

def solution(food_times, k):
    answer = 0
    i=0
    
    while True:
        
        if food_times.count(0)==len(food_times):#0이면이라는 조건을 담아야함.
          print(-1)
          break


        if k==0:#여기는 이거 맞아
          while True:
            if food_times[i]==0:
              i+=1
              if i==len(food_times):
                i=0
            else:
              break
          print(i+1)
          break    
            
        if food_times[i]!=0:
            food_times[i]=food_times[i]-1
            k-=1
        i+=1

        
        # if i==len(food_times):
        #   i=0 
        # if k==0:
        #   print(i+1)
        #   break        
        if i==len(food_times):
          i=0 
 
        print(food_times)
    
    return answer

solution(food_times,k)

#무지의 먹방 라이브~~~
#무지 조아
#내일 풀자~_~

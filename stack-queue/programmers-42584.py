
##단순 반복문으로 푼 것
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    for i in range(len(prices)):
        cnt=0
        for j in range(i+1,len(prices)):
            cnt+=1
            if prices[j]<prices[i]:
                break
        answer[i]=cnt
    return answer

##queue이용한 것
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer


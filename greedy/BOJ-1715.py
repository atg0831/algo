import heapq
import sys
N = int(input())
cards = [int(input()) for _ in range(N)]

heapq.heapify(cards)

answer = 0
while len(cards) > 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)

    sum_ = first + second
    heapq.heappush(cards,sum_)
    answer += sum_
print(answer)


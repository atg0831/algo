# Counter 이용해서 푼 것
from collections import Counter

N = int(input())
ownedcards = list(map(int, input().split()))

M = int(input())
cards = list(map(int, input().split()))

counter = Counter(ownedcards)
for card in cards:
    print(counter[card], end = " ")


#binary search 사용
N = int(input())
ownedcards = list(map(int, input().split()))

M = int(input())
cards = list(map(int, input().split()))



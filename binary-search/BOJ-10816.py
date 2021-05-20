# # Counter 이용해서 푼 것
# from collections import Counter

# N = int(input())
# ownedcards = list(map(int, input().split()))

# M = int(input())
# cards = list(map(int, input().split()))

# counter = Counter(ownedcards)
# for card in cards:
#     print(counter[card], end = " ")


#binary search 사용
N = int(input())
ownedcards = list(map(int, input().split()))

M = int(input())
cards = list(map(int, input().split()))


ownedcards.sort()

def left(key, idx, cnt):
    # print(cnt)
    if idx < 0:
        return
    if ownedcards[idx] == key:
        cnt[0] += 1
        left(key, idx - 1, cnt)
    # return cnt
def right(key, idx, cnt):
    # print(cnt)
    if idx == N:
        return
    
    if ownedcards[idx] == key:
        cnt[0] += 1
        right(key, idx + 1, cnt)
    
    # return cnt

# def find_same_val(key, idx, cnt):
#     cnt[0] += 1

#     if idx < 0 or idx == N:
#         return
    
#     if ownedcards[idx] != key:
#         return
#     # if ownedcards[idx] == key:
#     #     cnt[0] += 1
    
#     # else:
#     #     return

#     find_same_val(key, idx - 1, cnt)
#     find_same_val(key, idx + 1, cnt)

def binary_search(key):
    cnt = [0]
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if ownedcards[mid] == key:
            cnt[0] += 1
            left(key, mid - 1, cnt)
            right(key, mid + 1, cnt)
            # find_same_val(key, mid, cnt)
            print(cnt[0], end = ' ')
            return

        elif ownedcards[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
        
    print(0, end = ' ')
for key in cards:
    binary_search(key)
            

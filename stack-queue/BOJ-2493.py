from collections import deque
N = int(input())
towers = list(map(int, input().split()))

accepted = deque()
answer = []
for i, tower in enumerate(towers):
    if i == 0:
        accepted.append([i,tower])
        answer.append(0)
        continue

    while accepted:
        prev = accepted.pop()
        if prev[1] > tower:
            accepted.append(prev)
            accepted.append([i, tower])
            answer.append(prev[0]+1)
            break
        
        if len(accepted) == 0:
            accepted.append(prev)
            accepted.append([i, tower])
            answer.append(0)
            break

print(' '.join(map(str, answer)))











# accpeted = []
# for i in range(N-1, -1, -1):
#     if i != N-1:
#         if towers[i] <= towers[accpeted[-1][0]]:
#             accpeted.append([i, accpeted[-1][1]])
#             continue
        
#     for j in range(i-1, -1, -1):
#         if towers[i] <= towers[j]:
#             accpeted.append([i, j+1])
#             break

#         if j == 0:
#             accpeted.append([i, 0])

# accpeted.reverse()
# for _, val in accpeted:
#     print(val, end=" ")

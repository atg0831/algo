import sys
n = int(input())
INF = sys.maxsize
coins = [INF] * (n+1)
coins[0] = 0
# for i in range(1,n+1):
#     if i>=2:
#         if coins[i-2] != INF:
#             coins[i] = min(coins[i], coins[i-2]+1)
    
#     if i>=5:
#         if coins[i-5] != INF:
#             coins[i] = min(coins[i], coins[i-5]+1)

# if coins[n] == INF:
#     print(-1)
# else:
#     print(coins[n])

coins[2] = 1
coins[5] = 1

for i in range(6, n + 1):
    coins[i] = min(coins[i - 2] + 1, coins[i - 5] + 1)
if coins[n] >= INF:
    print(-1)
else:
    print(coins[n])


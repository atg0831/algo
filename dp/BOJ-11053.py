length = int(input())
A = [num for num in map(int, input().split())]

dp = [1] * (length)

for i in range(length):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

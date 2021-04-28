N = int(input())
pay = [0] + list(map(int, input().split()))
# dp = [i for i in range(1, N+1)]
dp = [0] * (N+1)
dp[1] = pay[1]


for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + pay[j])

print(dp[N])

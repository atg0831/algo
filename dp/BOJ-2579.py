stairs = int(input())
scores = []
for _ in range(stairs):
    scores.append(int(input()))

dp = [0] * (stairs)

dp[0] = scores[0]
dp[1] = max(dp[0]+scores[1], dp[1])
for i in range(2,stairs):
    dp[i]=max(dp[i-1], dp[i-2]) + scores[i]

print(dp[stairs-1])
# memoization 사용


def combination(n, r, dp):
    if dp[n][r] != 0:
        return dp[n][r]
    if r == 1:
        return n
    if n == r or r == 0:
        return 1

    dp[n][r] = combination(n-1, r, dp)+combination(n-1, r-1, dp)
    return dp[n][r]


T = int(input())
for test_case in range(T):
    r, n = map(int, input().split())
    dp = [[0 for _ in range(r+1)]for _ in range(n+1)]
    print(combination(n, r, dp))

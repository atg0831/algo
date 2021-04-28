n = int(input())

dp = [0] * (n+1)
dp[1] = 1
# dp[2] = 2
# dp[3] = 3


def fibo(n):
    if dp[n] != 0:
        return dp[n]

    elif n < 1:
        return 0

    elif n == 1:
        return dp[n]

    elif n == 2:
        dp[2] = 1
        return dp[n]

    elif n == 3:
        dp[3] = 2
        return dp[n]

    dp[n] = fibo(n-1)+fibo(n-2)
    return dp[n]


print(fibo(n))

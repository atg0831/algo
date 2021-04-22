import sys
input = sys.stdin
n, k = map(int, input.readline().split())

# solution 1
# nCr = n-1Cr + n-1Cr-1
def combination(n, r, dp):
    if dp[n][r] != 0:
        return dp[n][r]
    if r == 1:
        return n
    if n == r or r == 0:
        return 1

    dp[n][r] = combination(n-1, r, dp)+combination(n-1, r-1, dp)
    return dp[n][r]

dp = [[0 for _ in range(k+1)]for _ in range(n+1)]
print(combination(n-1, k-1, dp))


# solution 2
# 파스칼 삼각형 다 구현
tri = [[0, 1] for _ in range(n+2)]
tri[2].append(1)

for i in range(3, n+1):
    for j in range(1, i-1):
        tri[i].append(tri[i-1][j] + tri[i-1][j+1])
    tri[i].append(1)


print(tri[n][k])

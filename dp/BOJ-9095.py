T=int(input())
for test_case in range(T):
    n=int(input())
    dp=[0,1,2,4,7,0,0,0,0,0,0,0]
    for i in range(4,n+1):
        dp[i]=dp[i-3]+dp[i-2]+dp[i-1]

    print(dp[n])
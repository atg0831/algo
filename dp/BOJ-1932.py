N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]

cost = [[0 for _ in range(row)]for row in range(1, N+1)]
cost[0][0] = tri[0][0]
for i in range(1, N):
    for j in range(len(tri[i])):
        leftup = j - 1
        rightup = j  
        # 왼쪽 끝에 위치한다면
        if j == 0:
            cost[i][j] = tri[i][j] + cost[i-1][rightup]
        # 오른쪽 끝에 위치한다면
        elif j == len(tri[i]) - 1:
            cost[i][j] = tri[i][j] + cost[i-1][leftup]
        else:
            cost[i][j] = tri[i][j] + max(cost[i-1][rightup], cost[i-1][leftup])

print(max(cost[N-1]))



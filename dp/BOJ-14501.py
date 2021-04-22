N = int(input())
consult = [0]
for _ in range(N):
    T, P = map(int, input().split())
    consult.append((T, P))

# consult_profit = [0 for _ in range(N+1)]
profit = [0] * (N+1)
# 1. 그날 상담하기
# 2. 그날 상담하지 않기


for i in range(N+1):
    if i + consult[i][0] <= N:
        profit[i] = consult[i][1]
        for j in range(i):
            if j + consult[j][0] <= i:
                profit[i] = max(profit[i], profit[j] + consult[j][1])

print(max(profit))
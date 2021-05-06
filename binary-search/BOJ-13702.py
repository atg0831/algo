N, K = map(int, input().split())
alchols = []
for _ in range(N):
    alchols.append(int(input()))

answer = 0
start = 1
end = max(alchols)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for alchol in alchols:
        cnt += alchol // mid
    if cnt >= K:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
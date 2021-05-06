M, N = map(int, input().split())
snacks = list(map(int, input().split()))
answer = 0

if M == 1:
    answer = max(snacks)
else:
    start = 1
    end = max(snacks)

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for snack in snacks:
            cnt += snack // mid

        if cnt >= M:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

print(answer)

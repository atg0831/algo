N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

houses.sort()

print(houses)
start = 1
end = houses[-1] - houses[0]
answer = 0 
while start <= end:
    mid = (start + end) // 2

    cnt = 1
    prev_wifi = houses[0]
    for i in range(1, N):
        if houses[i] >= mid + prev_wifi:
            cnt += 1
            prev_wifi = houses[i]
    
    if cnt < C:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)

    
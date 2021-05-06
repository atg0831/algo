K, N = map(int, input().split())
wires = []
for _ in range(K):
    wires.append(int(input()))

max_ = max(wires)
start = 1
end = max_
answer = 0

while start <= end:
    mid = (start + end) // 2

    # cnt = 0
    # for wire in wires:
    #     cnt += wire // mid
    #더 빠르게 계산 가능
    cnt = sum([x // mid for x in wires])
    if cnt >= N:
        start = mid + 1
        answer = mid
    
    else:
        end = mid - 1

print(answer)
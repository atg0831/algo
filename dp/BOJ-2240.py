T, W = map(int, input().split())
loc = [0]
dp = [0] * (T+1)

for _ in range(T):
    loc.append(int(input()))
    
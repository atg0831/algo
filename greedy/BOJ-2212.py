N = int(input())
K = int(input())

sensors = list(map(int, input().split()))
sensors.sort()
dist = []

for i in range(1, N):
    dist.append(sensors[i] - sensors[i-1])

dist.sort()

answer = 0
for i in range(N-K):
    answer += dist[i]

print(answer)

# 좌표 정렬
# 1 3 |  6 6 7 9

# 각 좌표의 차이를 정렬
# 0 1 2 2 3   
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

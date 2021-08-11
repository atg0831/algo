from collections import deque
from sys import stdin
n, m, k, x = map(int, stdin.readline().split())

graph = [[]for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)

visited = [False for _ in range(n+1)]


citys = []
def bfs(start):
    visited[start] = True
    queue = deque([(start, 0)])
    city = 0
    while queue:
        u, cost = queue.popleft()

        if cost == k:
            city += 1
            citys.append(u)
            # print(u)
        for v in graph[u]:
            if not visited[v]:
                queue.append((v, cost+1))
                visited[v] = True
    return city

if bfs(x) == 0:
    print(-1)
else:
    citys.sort()
    for city in citys:
        print(city)



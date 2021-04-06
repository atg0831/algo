from collections import deque

N, M, V = map(int, input().split())
graph = [[]for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(N+1)


def dfs(vertex):
    visited[vertex] = True
    print(vertex, end=' ')

    for v in sorted(graph[vertex]):
        if not visited[v]:
            dfs(v)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        u = queue.popleft()
        print(u, end=' ')
        for v in sorted(graph[u]):
            if not visited[v]:
                queue.append(v)
                visited[v] = True


dfs(V)
visited = [False]*(N+1)
print()
bfs(V)

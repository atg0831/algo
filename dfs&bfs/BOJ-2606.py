N = int(input())
pairs = int(input())

computers = [[] for _ in range(N+1)]
# print(computers)
for _ in range(pairs):
    u, v = map(int, input().split())
    computers[u].append(v)
    computers[v].append(u)


visited = [False for _ in range(N+1)]
cnt = 0


def dfs(vertex):
    global cnt
    visited[vertex] = True
    for v in computers[vertex]:
        if not visited[v]:
            cnt += 1
            dfs(v)


dfs(1)
print(cnt)

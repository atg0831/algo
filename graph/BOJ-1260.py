from collections import deque
from sys import stdin
N, M, V = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dfs_ans = []


def dfs(vertex):
    print(vertex, end=' ')
    visited[vertex] = True
    # dfs_ans.append(vertex)

    sorted_graph = sorted(graph[vertex], key=lambda x: x)
    for next_vertex in sorted_graph:
        if not visited[next_vertex]:
            dfs(next_vertex)


bfs_ans = []


def bfs(start):
    queue = deque()
    visited[start] = True
    queue.append(start)
    # bfs_ans.append(start)
    print(start, end=' ')

    while queue:
        vertex = queue.popleft()

        for next_vertex in sorted(graph[vertex], key=lambda x: x):
            if visited[next_vertex] == False:
                visited[next_vertex] = True
                queue.append(next_vertex)
                # bfs_ans.append(next_vertex)
                print(next_vertex, end=' ')


visited = [False]*(N+1)
dfs(V)
# print(dfs_ans)
visited = [False]*(N+1)
print()
bfs(V)
# print(bfs_ans)

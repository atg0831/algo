import sys
T = int(input())
sys.setrecursionlimit(10**7)
for _ in range(T):
    N = int(input())
    data = list(map(int, sys.stdin.readline().split()))
    data = [0]+data

    visited = [0]*(N+1)
    cycle_start = []

    def dfs(vertex):
        if visited[vertex] == 1:
            cycle_start.append(vertex)
            return

        if vertex >= N+1:
            return

        visited[vertex] += 1
        dfs(data[vertex])

    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)

    print(len(cycle_start))

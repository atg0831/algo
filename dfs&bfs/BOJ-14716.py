import sys
sys.setrecursionlimit(10**8)
M, N = map(int, input().split())
banner = []
for _ in range(M):
    banner.append(sys.stdin.readline().rstrip().split())

dir = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
visited = [[False for _ in range(N)]for _ in range(M)]


def possible_path(x, y):
    if (0 <= x < M) and (0 <= y < N):
        return True

    return False


def dfs(posx, posy):
    visited[posx][posy] = True

    for dirx, diry in dir:
        nextx = posx+dirx
        nexty = posy+diry

        if possible_path(nextx, nexty):
            if not visited[nextx][nexty] and banner[nextx][nexty] == '1':
                dfs(nextx, nexty)


cnt = 0
for i in range(M):
    for j in range(N):
        if not visited[i][j] and banner[i][j] == '1':
            dfs(i, j)
            cnt += 1

print(cnt)

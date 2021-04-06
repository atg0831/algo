import sys
sys.setrecursionlimit(10**8)
N = int(input())

lines = []

for _ in range(N):
    lines.append(list(sys.stdin.readline().rstrip()))

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
visited = [[False for _ in range(N)]for _ in range(N)]


def possible_path(x, y):
    if (0 <= x < N) and (0 <= y < N):
        return True

    return False


def dfs(curx, cury):
    visited[curx][cury] = True
    cur = lines[curx][cury]

    for dirx, diry in dir:
        nextx = curx+dirx
        nexty = cury+diry
        if possible_path(nextx, nexty):
            if not visited[nextx][nexty]:
                if cur == lines[nextx][nexty]:
                    dfs(nextx, nexty)


normal = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            normal += 1


color_weakness = 0
visited = [[False for _ in range(N)]for _ in range(N)]
for i in range(N):
    for j in range(N):
        if lines[i][j] == 'G':
            lines[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            color_weakness += 1

print(normal, color_weakness)

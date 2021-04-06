import sys
from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def possible_path(x, y):
    if (0 <= x < N) and (0 <= y < M) and maze[x][y] == 1:
        return True

    return False


def bfs(posx, posy, min_):
    queue = deque()
    level = 1
    queue.append((posx, posy, level))
    visited[posx][posy] = True

    while queue:
        curx, cury, level = queue.popleft()

        if curx == N-1 and cury == M-1:
            if min_ > level:
                min_ = level
        level += 1
        for dirx, diry in dir:
            nextx = curx+dirx
            nexty = cury+diry
            if possible_path(nextx, nexty):
                if not visited[nextx][nexty]:
                    queue.append((nextx, nexty, level))
                    visited[nextx][nexty] = True

    print(min_)


min_ = 1111111111111111111
bfs(0, 0, min_)

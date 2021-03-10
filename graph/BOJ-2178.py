from collections import deque
from sys import stdin
N, M = map(int, stdin.readline().split())

maze = []
for i in range(N):
    maze.append(list(map(int, (stdin.readline().rstrip()))))

goal = [N-1, M-1]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def possible_path(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    else:
        if maze[x][y] == 1:
            return True
        else:
            return False


visited = [[False]*(M) for _ in range(N)]
level = [[0]*M for _ in range(N)]


def bfs(startx, starty, depth, min_level):
    queue = deque()
    queue.append((startx, starty))
    visited[startx][starty] = True
    level[startx][starty] = 1

    while queue:
        curx, cury = queue.popleft()
        if curx == goal[0] and cury == goal[1]:
            if min_level > level[curx][cury]:
                min_level = level[curx][cury]

        for dirx, diry in dir:
            nextx = curx+dirx
            nexty = cury+diry
            if possible_path(nextx, nexty):
                if visited[nextx][nexty] == False:
                    queue.append((nextx, nexty))
                    visited[nextx][nexty] = True
                    level[nextx][nexty] = level[curx][cury]+1

    print(min_level)


INF = 1000000000
bfs(0, 0, 1, INF)

from itertools import combinations
from collections import deque

import copy
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]


def is_possible_wall(maps):
    wallable = []
    virusable = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                wallable.append((i, j))
            elif maps[i][j] == 2:
                virusable.append((i,j))
    return wallable, virusable


a = []


def solution(wallable, virusable):
    safety_zone = []
    for cases in list(combinations(wallable, 3)):
        # print(cases)
        temp = copy.deepcopy(maps)
        # print(temp)
        # print(cases[2][0])
        for i in range(3):
            temp[cases[i][0]][cases[i][1]] = 1
        # print(temp)

        safety_zone.append(max_safetyzone(temp, virusable))

    return (safety_zone)


def possible_path(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True

    return False


dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
visited = [[False for _ in range(M)]for _ in range(N)]


def spread_virus(temp, virusable):
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        curx, cury = queue.popleft()
        if temp[curx][cury] != 1212132:
            for dirx, diry in dir:
                pathx = curx + dirx
                pathy = cury + diry
                if possible_path(pathx, pathy) and not visited[pathx][pathy]:
                    if temp[pathx][pathy] == 2:
                        queue.append((pathx, pathy))
                        temp[curx][cury] = 2
                        visited[pathx][pathy] = True

    return temp


def max_safetyzone(temp, virusable):
    cnt = 0
    after = spread_virus(temp, virusable)
    for line in after:
        for element in line:
            if element == 0:
                cnt += 1

    return cnt


# wallable: maps 좌표 중에서 0인 곳(벽으로 만들 수 있는 좌표)
wallable, virusable = is_possible_wall(maps)
print(solution(wallable, virusable))

from collections import deque
import sys
sys.setrecursionlimit(10**7)
N = int(input())
map = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
visited = [[False] * N for _ in range(N)]


def possible_path(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    else:
        if map[x][y] == 1 and visited[x][y] == False:
            return True

        return False


def dfs(posx, posy, each_house):
    visited[posx][posy] = True
    for dirx, diry in dir:
        nextx = posx+dirx
        nexty = posy+diry

        if possible_path(nextx, nexty):
            each_house += 1
            each_house = dfs(nextx, nexty, each_house)

    return each_house


total_num = 0
houses = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and map[i][j] == 1:
            total_num += 1
            each_house = 1
            each_house = dfs(i, j, each_house)
            houses.append(each_house)

print(total_num)

for element in sorted(houses, key=lambda x: x):
    print(element)

N = int(input())
bamboos = [list(map(int, input().split())) for _ in range(N)]

result = []
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def possible_path(x, y, visited):
    if 0 <= x < N and 0 <= y < N and visited[x][y] == False:
        return True
    return False
# print(visited)


def dfs(x, y, visited, cnt):
    visited[x][y] = True
    curbamboo = bamboos[x][y]
    for dirx, diry in dir:
        nextx, nexty = dirx + x, diry + y

        if possible_path(nextx, nexty, visited):
            if curbamboo < bamboos[nextx][nexty]:
                dfs(nextx, nexty, visited, cnt+1)
            
        
        result.append(cnt)
        # print(result)
for row in range(N):
    for col in range(N):
        visited = [[False] * len(bamboos[row])for row in range(N)]
        dfs(row, col, visited, 1)

print(max(result))

from collections import deque
M, N = map(int, input().split())
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))


def possible_path(row, col):
    if (0 <= row < N) and (0 <= col < M):
        return True

    return False


visited = [[False for _ in range(M)]for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def bfs():
    while queue:
        row, col, level = queue.popleft()
        for dir_row, dir_col in dir:
            next_row = row + dir_row
            next_col = col + dir_col

            if possible_path(next_row, next_col):
                if not visited[next_row][next_col] and box[next_row][next_col] == 0:
                    visited[next_row][next_col] = True
                    box[next_row][next_col] = 1
                    queue.append((next_row, next_col, level+1))

    for b in box:
        if 0 in b:
            return -1
    return level


queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j, 0))
            visited[i][j] = True

print(bfs())

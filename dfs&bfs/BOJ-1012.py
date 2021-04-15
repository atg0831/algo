import sys
sys.setrecursionlimit(10**8)
T = int(input())

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def possible_path(row, col):
    if (0 <= row < N) and (0 <= col < M) and not visited[row][col]:
        return True

    return False


def dfs(row, col):
    visited[row][col] = True

    for dir_row, dir_col in dir:
        next_row = row + dir_row
        next_col = col + dir_col

        if possible_path(next_row, next_col):
            if maps[next_row][next_col] == 1:
                dfs(next_row, next_col)


for _ in range(T):
    M, N, K = map(int, input().split())
    maps = [[0 for _ in range(M)]for _ in range(N)]
    for _ in range(K):
        col, row = map(int, input().split())
        maps[row][col] = 1

    visited = [[False for _ in range(M)]for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)

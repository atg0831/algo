from collections import deque

N = int(input())
space = [list(map(int, input().split()))for _ in range(N)]


init_x, init_y = -1, -1

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            init_x, init_y = i, j
            space[i][j] = 0


dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def possible_path(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True

    return False


def bfs(x, y):
    # queue는 현재위치에서 이동 가능한 좌표 모음
    queue = deque([(x, y)])
    visited = set([(x, y)])
    shark_size = 2
    eat_num = 0
    eat_current = False
    time = 0
    answer = 0

    while queue:
        # 위, 왼쪽 우선순위에 있으므로 sorting해서 queue에 집어넣어준다
        queue = deque(sorted(queue))
        for _ in range(len(queue)):
            curx, cury = queue.popleft()

            if space[curx][cury] != 0 and space[curx][cury] < shark_size:
                eat_num += 1
                space[curx][cury] = 0

                if eat_num == shark_size:
                    shark_size += 1
                    eat_num = 0

                queue = deque()
                visited = set([(x, y)])
                eat_current = True

                answer = time

            for dirx, diry in dir:
                nextx, nexty = curx + dirx, cury + diry

                if possible_path(nextx, nexty):
                    if nextx not in visited and nexty not in visited:
                        if space[nextx][nexty] <= shark_size:
                            queue.append((nextx, nexty))
                            visited.add((nextx, nexty))

            # 현재위치에서 먹었으면 반복문 break
            if eat_current:
                eat_current = False
                break

        time += 1

    return answer



print(bfs(init_x, init_y))

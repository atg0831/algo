from collections import deque
F, S, G, U, D = map(int, input().split())

entire = F
goal = G
start = S

visited = [False for _ in range(entire+1)]
dir = [U, -D]


def possible_path(floor):
    if (1 <= floor <= F):
        return True

    return False


def bfs(start, level):
    queue = deque()
    queue.append((start, level))
    visited[start] = True

    while queue:
        cur_floor, level = queue.popleft()
        if cur_floor == goal:
            return level
        level += 1

        for step in dir:
            next_floor = cur_floor + step
            if possible_path(next_floor):   
                if not visited[next_floor]:
                    queue.append((next_floor, level))
                    visited[next_floor] = True
    return -1


ans = bfs(start, 0)
if ans == -1:
    print("use the stairs")
else:
    print(ans)

from collections import deque

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    priorities = deque()
    for i, priority in enumerate(list(map(int, input().split()))):
        priorities.append((i, priority))

    target = priorities[M]
    cnt = 1
    max_ = max(priorities, key=lambda x: x[1])
    while priorities:
        if max_ == target:
            print(cnt)
            break

        elif max_[1] <= priorities[0][1]:
            priorities.popleft()
            max_ = max(priorities, key=lambda x: x[1])
            cnt += 1

        else:
            priorities.append(priorities.popleft())


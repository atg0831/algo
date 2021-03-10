from collections import deque
import sys

A, P = map(str, input().split())

# list(str(A))한 이유는 각 자리수 제곱하고 더할 때 편하게 하기 위해
A = list(A)
P = int(P)


def cal_each(data, idx):
    result = 0
    for element in data[idx]:
        result += int(element)**P

    return result


stop = False
def dfs(idx, data, next):
    global stop
    if idx >= len(data):
        return

    # print(data[idx],next)
    if next == data[idx]:
        print(idx)
        stop = True
        return

    dfs(idx+1, data, next)


data = deque()
data.appendleft(A)
while True:
    next = cal_each(data, -1)
    # list(str(next))한 이유도 각 자리수 때서 계산 편리위해
    next = list(str(next))
    # print(next)
    dfs(0, data, next)
    if stop == True:
        # print(cnt)
        break
    data.append(next)
    # print(data)

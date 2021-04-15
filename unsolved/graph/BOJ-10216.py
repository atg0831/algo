# https://www.hyesungoh.xyz/Algorithm/BOJ-10216-Python/ 참고
# https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html

# union-find(by rank)
import sys
input = sys.stdin.readline


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a == parent_b:
        return

    if rank[parent_a] < rank[parent_b]:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a
        if rank[parent_a] == rank[parent_b]:
            rank[parent_a] += 1


def find(node):
    if parent[node] == node:
        return node

    p = find(parent[node])
    parent[node] = p
    return p


for _ in range(int(input())):
    n = int(input())

    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    ypos = [0 for i in range(n)]
    xpos = [0 for i in range(n)]
    radius = [0 for i in range(n)]

    for i in range(n):
        y, x, r = map(int, input().split())
        ypos[i] = y
        xpos[i] = x
        radius[i] = r

    ans = n
    for i in range(n):
        for j in range(i+1, n):
            ydif = ypos[i] - ypos[j]
            xdif = xpos[i] - xpos[j]
            r = radius[i] + radius[j]

            if (ydif*ydif + xdif*xdif) <= (r*r):
                if find(i) != find(j):
                    union(i, j)
                    ans -= 1

    print(ans)

# union-find 기본
input = sys.stdin.readline


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a != parent_b:
        parent[parent_b] = parent_a


def find(node):
    if parent[node] == node:
        return node

    p = find(parent[node])
    parent[node] = p
    return p


for _ in range(int(input())):
    n = int(input())

    parent = [i for i in range(n)]
    ypos = [0 for i in range(n)]
    xpos = [0 for i in range(n)]
    radius = [0 for i in range(n)]

    for i in range(n):
        y, x, r = map(int, input().split())
        ypos[i] = y
        xpos[i] = x
        radius[i] = r

    ans = n
    for i in range(n):
        for j in range(i+1, n):
            ydif = ypos[i] - ypos[j]
            xdif = xpos[i] - xpos[j]
            r = radius[i] + radius[j]

            if (ydif*ydif + xdif*xdif) <= (r*r):
                if find(i) != find(j):
                    union(i, j)
                    ans -= 1

    print(ans)

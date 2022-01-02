import sys
n, m = map(int, sys.stdin.readline().split(' '))

selected = [0 for _ in range(m)]
visited = [False for _ in range(n+1)]

def recur(k):
    if k == m:
        for x in selected:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if not visited[i]:
                selected[k] = i
                visited[i] = True
                recur(k+1)
                visited[i] = False

recur(0)
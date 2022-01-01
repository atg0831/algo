import sys
n, m = map(int, sys.stdin.readline().split(' '))

selected = [0 for _ in range(m)]

def recur(k):
    if k == m:
        for x in selected:
            print(x, end = ' ')
        print()
    else:
        for cand in range(1, n + 1):
            selected[k] = cand
            recur(k + 1)

recur(0)
from sys import stdin
N = int(input())
T = [-1 for _ in range(N+1)]
P = [0 for _ in range(N+1)]
for i in range(1, N+1):
    T[i], P[i] = map(int, stdin.readline().split())

selected = []
maxlist = []


def sol(start):
    if start == N+1:
        maxlist.append(sum(selected))
        return

    if start>N+1:
        return
        
    if start+T[start] <= N+1:
        selected.append(P[start])
        sol(start+T[start])
        selected.pop()
    if start+1 <= N+1:
        sol(start+1)


sol(1)
print(max(maxlist))
# next i+T[i]

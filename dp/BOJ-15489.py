import sys
input = sys.stdin
r, c, w = map(int, input.readline().split())

tri = [[0, 1] for _ in range(r+w+1)]
tri[2].append(1)

for i in range(3, r+w):
    for j in range(1, i-1):
        tri[i].append(tri[i-1][j] + tri[i-1][j+1])
    tri[i].append(1)

answer = 0
for i in range(r, r+w):
    for j in range(i-r+1):
        answer += tri[i][c+j]

if r+w == 2:
    answer = 3
print(answer)

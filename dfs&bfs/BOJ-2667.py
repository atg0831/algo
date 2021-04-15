import sys
N=int(input())

houses = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dir = [(-1,0),(1,0),(0,1),(0,-1)]
def posiible_path(x,y):
    if (0<=x<N) and (0<=y<N):
        return True

    return False

def dfs(x,y,selected):
    visited[x][y]=True
    selected.append((x,y))

    for dirx, diry in dir:
        nextx = x+dirx
        nexty = y+diry

        if posiible_path(nextx,nexty):
            if not visited[nextx][nexty] and houses[nextx][nexty]==1:
                dfs(nextx,nexty,selected)

num_of_houses=0
kind_of_houses=[]
visited=[[False for _ in range(N)]for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and houses[i][j]==1:
            selected=[]
            dfs(i,j,selected)
            num_of_houses+=1
            kind_of_houses.append(len(selected))

print(num_of_houses)
for num in sorted(kind_of_houses):
    print(num)

# https://www.acmicpc.net/board/view/27386
# 참고할만한 풀이방법(이문제랑2206번 비슷하다)
import sys
# sys.setrecursionlimit(10**8)
N,M=map(int,input().split())
hx,hy=map(int,input().split())
ex,ey=map(int,input().split())

maze=[list(map(int,sys.stdin.readline().split()))for _ in range(N)]
visited=[[False for _  in range(M)]for _ in range(N)]
dir=[(-1,0),(1,0),(0,1),(0,-1)]

def possible_path(x,y):
    if (0<=x<N) and (0<=y<M):
        return True

    return False
INF=111111111111
min_=INF

from collections import deque

def bfs(posx,posy,steps,chance):
    queue=deque()
    queue.append((posx,posy,steps,chance))
    visited[posx][posy]=True
    global min_
    while queue:
        curx,cury,steps,chance=queue.popleft()

        if curx==ex-1 and cury==ey-1:
            return steps
        
        for dirx, diry in dir:
            nextx=curx+dirx
            nexty=cury+diry

            if possible_path(nextx,nexty):
                if not visited[nextx][nexty]:
                    if maze[nextx][nexty]==1 and chance==1:
                        queue.append((nextx,nexty,steps+1,chance-1))
                        visited[nextx][nexty]=True
                    
                    elif maze[nextx][nexty]==0:
                        queue.append((nextx,nexty,steps+1,chance))
                        visited[nextx][nexty]=True
    return -1
    

ans=bfs(hx-1,hy-1,0,1)
print(ans)

# chancex=0
# chancey=0
# def dfs(posx,posy,steps,cnt):
#     global min_
#     global chancex
#     global chancey
#     visited[posx][posy]=True

#     if posx==ex-1 and posy==ey-1:
#         if min_>steps:
#             min_=steps
#         return

#     for dirx, diry in dir:
#         nextx=posx+dirx
#         nexty=posy+diry

#         if possible_path(nextx,nexty):
#             if not visited[nextx][nexty]:
#                 if maze[nextx][nexty]==1 and cnt==0:
#                     # maze[nextx][nexty]=0
#                     cnt+=1
#                     dfs(nextx,nexty,steps+1,cnt)
                    

#                 elif maze[nextx][nexty]==0:
#                     dfs(nextx,nexty,steps+1,cnt)
#                     # visited[nextx][nexty]=False
#                     cnt-=1
                
#                 visited[nextx][nexty]=False



# maze[2][1]=0
# dfs(hx-1,hy-1,0,0)
# # print(min_)
# for i in range(N):
#     for j in range(M): 
#         if maze[i][j]==1:
#             maze[i][j]=0
#             dfs(hx-1,hy-1,0)
#             visited[hx-1][hy-1]=False
#             maze[i][j]=1
        
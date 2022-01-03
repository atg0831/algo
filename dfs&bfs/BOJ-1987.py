# import sys
# R,C=map(int,input().split())
# boards=[list(map(str,sys.stdin.readline().rstrip()))for _ in range(R)]

# def possible_path(x,y):
#     if (0<=x<R) and (0<=y<C):
#         return True
    
#     return False

# dir=[(-1,0),(1,0),(0,1),(0,-1)]

# max_=-1
    
# def bfs(posx,posy,cnt):
#     queue=set([(posx,posy,cnt,boards[posx][posy])])
#     # queue.add((posx,posy,cnt,boards[posx][posy]))

#     while queue:
#         posx,posy,cnt,visited=queue.pop()
#         global max_
#         if cnt>max_:
#             max_=cnt
        
#         if max_==26:
#             return 26
#         for dirx,diry in dir:
#             nextx=posx+dirx
#             nexty=posy+diry
#             if possible_path(nextx,nexty) and boards[nextx][nexty] not in visited:
#                 queue.add((nextx,nexty,cnt+1,visited+boards[nextx][nexty]))

# bfs(0,0,1)
# print(max_)



from collections import deque
import sys
R, C = map(int, input().split())
boards = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]

visited = [[False for _ in range(C)] for _ in range(R)]
# alpha_visited = [False for _ in range(26)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def possible_path(x, y):
    if 0<=x<R and 0<=y<C:
        return True
    
    return False

max_ = 0
def bfs(x, y):
    global max_
    visited[x][y] = True
    queue = deque([(x, y, boards[x][y], 1)])
    # alpha_visited[ord(boards[x][y]) - 65] = True

    while queue:
        curx, cury, alpha_visited, cnt = queue.popleft()
        
        for dirx, diry in dir:
            nextx, nexty = curx + dirx, cury + diry

            if possible_path(nextx, nexty):
                nextalpha = boards[nextx][nexty]
                if nextalpha not in alpha_visited:
                    queue.append(([nextx, nexty, alpha_visited + nextalpha, cnt + 1]))
                    visited[nextx][nexty] = True
                    # alpha_visited[ord(nextalpha)- 65] = True
            
    if max_ < cnt:
        max_ = cnt
    return max_

print(bfs(0,0))
                



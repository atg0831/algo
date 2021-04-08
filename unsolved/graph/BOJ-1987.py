import sys
R,C=map(int,input().split())
boards=[list(map(str,sys.stdin.readline().rstrip()))for _ in range(R)]

def possible_path(x,y):
    if (0<=x<R) and (0<=y<C):
        return True
    
    return False

dir=[(-1,0),(1,0),(0,1),(0,-1)]

max_=-1
    
def bfs(posx,posy,cnt):
    queue=set([(posx,posy,cnt,boards[posx][posy])])
    # queue.add((posx,posy,cnt,boards[posx][posy]))

    while queue:
        posx,posy,cnt,visited=queue.pop()
        global max_
        if cnt>max_:
            max_=cnt
        
        if max_==26:
            return 26
        for dirx,diry in dir:
            nextx=posx+dirx
            nexty=posy+diry
            if possible_path(nextx,nexty) and boards[nextx][nexty] not in visited:
                queue.add((nextx,nexty,cnt+1,visited+boards[nextx][nexty]))

bfs(0,0,1)
print(max_)

# DFS로는 시간초과를 피하기 어려운데 방법이??dict도 값을 바꿀 때 시간복잡도는 상수타임이자만
# 실제 시간은 좀 걸리는듯??

# from collections import deque
# visited={}
# v=[[False for _ in range(C)]for _ in range(R)]
# for board in boards:
#     for alphabet in board:
#         visited[alphabet]=visited.get(alphabet,False)

# print(visited)
# selected=[]
# max_=-1
# def dfs(posx,posy,cnt):
#     cur_alphabet=boards[posx][posy]
#     visited[cur_alphabet]=True
#     v[posx][posy]=True
#     global max_

#     max_=max(max_,cnt)
#     if max_==26:
#         return 
    
#     for dirx,diry in dir:
#         nextx=posx+dirx
#         nexty=posy+diry
        
#         if not possible_path(nextx,nexty):
#             continue

#         next_alphabet=boards[nextx][nexty]
#         if not visited[next_alphabet]:
#             dfs(nextx,nexty,cnt+1)
#             visited[next_alphabet]=False
#             v[nextx][nexty]=False
# dfs(0,0,1)
# print(max_)

# import sys

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

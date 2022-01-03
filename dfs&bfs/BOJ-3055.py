from collections import deque
r, c = map(int, input().split())

maps = [list(input())for _ in range(r)]

visited = [[False for _ in range(c)]for _ in range(r)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def w_possible_path(wx,wy, curmap):
    if 0<=wx<r and 0<=wy<c and curmap[wx][wy] == '.':
        return True
    
    return False

def s_possible_path(x, y, curmap):
    if 0<=x<r and 0<=y<c and not visited[x][y] and curmap[x][y] != 'X' and maps[x][y] != '*':
        return True
    
    return False

def bfs(wx, wy, sx, sy, water_list):
    time = 0
    visited[sx][sy] = True
    queue = deque([(water_list, sx, sy, time, maps,)])

    while queue:
        water_list, cursx, cursy, curtime, curmap = queue.popleft()
        # water 침수 과정 먼저
        # for dirx, diry in dir:

        if maps[cursx][cursy] == 'D':
            return curtime
        for dirx, diry in dir:
            for water in water_list:
                nextwx, nextwy = water[0]+dirx, water[1]+diry
                if w_possible_path(nextwx, nextwy, curmap):
                    curmap[nextwx][nextwy] = '*'
                    water_list.append((nextwx, nextwy))
        for dirx, diry in dir:
            nextsx, nextsy = cursx+dirx, cursy+diry

            if s_possible_path(nextsx, nextsy, curmap):
                visited[nextsx][nextsy]= True
                curmap[nextsx][nextsy]='.'
                queue.append((nextwx, nextwy, nextsx, nextsy, curtime+1, curmap))

    return "KAKTUS"


# print(bfs(
        
    

from collections import deque
import sys

def move_return(x,y):
    return [x+2,y+1],[x+2,y-1],[x+1,y+2],[x+1,y-2],[x-2,y+1],[x-2,y-1],[x-1,y+2],[x-1,y-2]

     
def bfs(pos_x,pos_y,goal_x,gaol_y,count):
    q=deque()
    q.append([pos_x,pos_y,count])
    while q:

        x,y,c=q.popleft()
        if x==goal_x and y==gaol_y:
            return c
        # make_adjaceny(x,y)
        color[x][y]=BLACK
        count=c+1
        pos=move_return(x,y)

        for i in range(8):
            if(pos[i][0]<0 or pos[i][1]<0 or pos[i][0]>L-1 or pos[i][1]>L-1):
                continue

            if color[pos[i][0]][pos[i][1]]==WHITE:               
                q.append([pos[i][0],pos[i][1],count])
                color[pos[i][0]][pos[i][1]]=GRAY

                
T=int(input())

WHITE=32
GRAY=16
BLACK=8
answer=[]
for test_case in range(T):
    L=int(input())
    # adj_mat=[[0 for _ in range(L)]for _ in range(L)]
    color=[[WHITE for _ in range(L)]for _ in range(L)]
    current_x,current_y=list(map(int,input().split()))
    
    goal_x,gaol_y=list(map(int,input().split()))
    count=0
    answer.append((bfs(current_x,current_y,goal_x,gaol_y,count)))

for i in range(T):
    print(answer[i])
    

       


# def init_adjacency():
#     adj_mat=[[0 for _ in range(L)]for _ in range(L)]
#     return adj_mat

# def make_adjaceny(pos_x,pos_y):
#     adj_mat[pos_x+2,pos_y+1]=1
#     adj_mat[pos_x+2,pos_y-1]=1
#     adj_mat[pos_x+1,pos_y+2]=1
#     adj_mat[pos_x+1,pos_y-2]=1
#     adj_mat[(pos_x-2),pos_y+1]=1
#     adj_mat[(pos_x-2),pos_y-1]=1
#     adj_mat[(pos_x-1),pos_y+2]=1
#     adj_mat[(pos_x-1),pos_y-2]=1

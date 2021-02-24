def bfs(current_pos,final_pos,dir,l,visited):
    level=0
    queue=[[current_pos,level]]
    
    while queue:
        current_pos=queue.pop(0)
        current_level=current_pos[1]
        current_x=current_pos[0][0]
        current_y=current_pos[0][1]

        # visited[current_x][current_y]=True        

        # print(current_pos)
        if current_x==final_pos[0] and current_y==final_pos[1]:
            return current_level
        current_level+=1    
        for i in range(8):
            next_x=current_x+dir[i][0]
            next_y=current_y+dir[i][1]
            
            if next_x<0 or next_y<0 or next_x>l-1 or next_y>l-1:
                continue

            if visited[next_x][next_y]==False:
                next_pos=[next_x,next_y]
                queue.append([next_pos,current_level])
                visited[next_x][next_y]=True
                
                
if __name__ == "__main__":
    test_case=int(input())

    dir=[[-2,1],[-1,2],[-2,-1],[-1,-2],[1,2],[2,1],[1,-2],[2,-1]]
        
    for _ in range(test_case):
        l=int(input())
        current_pos=list(map(int,input().split()))
        final_pos=list(map(int,input().split()))
        visited=[[False]*l for _ in range(l)]        
        print(bfs(current_pos,final_pos,dir,l,visited))
        

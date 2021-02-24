import sys
N=int(sys.stdin.readline())
adj_mat=[]
result_list=[[0 for _ in range(N)]for _ in range(N)]
WHITE=32
GRAY=16
BLACK=8
count=0

color=[[WHITE for _ in range(N)]for _ in range(N)]  
for row in range(N):
    adj_mat.append(list(map(int,sys.stdin.readline().split())))

# DFS
def dfs(index,start,count):
    color[index][start]=BLACK
    
    for i in range(N):
        v=adj_mat[start][i]
        if(index==i) and v==1 and count>0:
            result_list[index][index]=1
           
        if (color[index][i]==WHITE and v==1):
            result_list[index][i]=1
            count+=1
            dfs(index,i,count)  
            
for i in range(N):
    dfs(i,i,count)
    
for row in range(N):
    for col in result_list[row]:
        print(col,end=' ')
    print()

    
    ######color 이차원 배열로 할 필요 없이 반복문 돌릴때 갱신하면 되고 
    ##count 변수 역시 필요가 없다

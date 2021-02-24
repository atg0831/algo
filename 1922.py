from collections import deque

BLACK = 8
WHITE = 16
GRAY = 32

N=int(input())
M=int(input())

graph = [[] for _ in range(N + 1)]
color = [WHITE for _ in range(N + 1)]
check_color=[BLACK for _ in range(N+1)]
check_color[0]=WHITE


# make adjacency list
for _ in range(M):
    from_vertex, to_vertex,w = list(map(int, input().split()))
    graph[from_vertex].append([w,to_vertex])
    graph[to_vertex].append([w,from_vertex])

# heqpq사용 
import heapq 
def prim(start):
    min_sum=0

    color[start]=BLACK
    queue=[]
 
    for u in sorted(graph[start],key=lambda x : x[0]):
        heapq.heappush(queue,u)

    
    while queue:
        cost,vertex=heapq.heappop(queue)
        if(color[vertex]==WHITE):
            color[vertex]=BLACK
            min_sum+=cost
            for u in sorted(graph[vertex],key=lambda x : x[0]):
                heapq.heappush(queue,u)
        
        # 모든 vertex들 방문했다면 종료
        if(color==check_color):
            return min_sum


print(prim(1))            
 
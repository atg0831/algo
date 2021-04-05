from collections import deque

def solution(n, edge):
    answer = 0
    adj_list=[[] for _ in range(n+1)]
    
    for from_,to_ in edge:
        adj_list[from_].append(to_)
        adj_list[to_].append(from_)
    
    
    visited=[False for _ in range(n+1)]
    dist=[]
    level=0

    def bfs(vertex,level):
        visited[vertex]=True
        queue=deque()
        queue.append((vertex,level))
        
        while queue:
            u,level=queue.popleft()            
            level+=1
            
            for v in adj_list[u]:
                if not visited[v]:
                    visited[v]=True
                    queue.append((v,level))
                    dist.append((v,level))
    
        return level-1
    
    
    level=bfs(1,0)    
    for v,l in dist:
        if l<level:
            continue
        answer+=1
    return answer
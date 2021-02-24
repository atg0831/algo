import sys
from collections import deque

N=int(input())
graph=[[] for _ in range(N+1)]
WHITE=1
BLACK=0
GRAY=-1
color=[WHITE] * (N+1)

for u in range(1,N+1):
    i=list(map(int,input().split()))
    for j in range(1,i[0]+1):
        graph[u].append(i[j])


def bfs(start,det):
    q=deque()
    color[start]=BLACK
    q.append([start,det])

    while q:
        v,det=q.popleft()
        color[v]=BLACK
        if  det==1 :
            B.append(v)
        else :
            W.append(v)

        det*=-1
        for k in graph[v]:
            if color[k]==WHITE:
                color[k]=GRAY
                q.append([k,det])
det=1###det==1이면 청팀,-1이면 백팀
B=[]###청팀
W=[]###백팀
for i in range(1,N+1):
    if i not in B and i not in W:####청팀과 백팀으로 나누어지지 않은 vertex만 bfs
    # if color[i]==WHITE:####방문하지 않은 vertex만 bfs해도 가능
        bfs(i,det)
    # print(B)
    # print(W)

len_B=len(B)
len_W=len(W)
B.sort()
W.sort()
print(len_B)
for i in range(len_B):
    print(B[i],end=' ')
print()
print(len_W)
for j in range(len_W):
    print(W[j],end=' ')


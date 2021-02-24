import sys

r=sys.stdin.readline
N=int(r())
WHITE=0
GRAY=2
BLACK=1
adj_list=[0]


for u in range(1,N+1):
    v=int(r())
    adj_list.append(v)


def dfs(start,index):
    color[start]=BLACK
    v=adj_list[start]
    # print(v)
    if color[v]==WHITE:
        dfs(v,index)
    elif v==index:
        ans_list.append(v)
 
ans_list=[]
for i in range(1,N+1):
    color=[WHITE for _ in range(N+1)]
    dfs(i,i)
    

print(len(ans_list))
for element in ans_list:
    print(element)


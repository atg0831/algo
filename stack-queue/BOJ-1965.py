from collections import deque

T=int(input())

for test_case in range(T):
    N,M=map(int,input().split())
    priority=list(map(int,input().split()))
    target=priority[M]

    p=deque()
    for idx,val in enumerate(priority):
        p.append((idx,val))
    p=sorted(p,key=lambda x : x[1],reverse=True)

    cnt=0
    prev=(0,0)
    # while p:
    #     first=p.popleft()
    #     if first[1]==target:
    #         if prev[1]==first[1]:

    #         cnt+=1  
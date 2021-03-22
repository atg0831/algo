# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean
# import sys
# sys.setrecursionlimit(10**8)
# N=int(input())
# path=list(map(int,input()))

# cnt=0
# def my_recur(idx,dist):
#     global cnt
#     if idx>=N:
#         return

#     if path[idx]==0:
#         return


#     if dist==N-1:
#         cnt+=1
#         return

#     if path[idx]==0:
#         return

#     my_recur(idx+1,dist+1)
#     my_recur(idx+2,dist+2)


# my_recur(0,0)
# print(cnt)


# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean
# genre_list=['A','B','C','D','E']
# ratings=list(map(float,input().split()))
# ratings_dict={}
# for i,genre in enumerate(genre_list):
# 	ratings_dict[genre]=ratings_dict.get(genre,0.0)+ratings[i]

# N,M=map(int,input().split())

# info=[list(map(str,input())) for _ in range(N)]
# genres=[list(map(str,input())) for _ in range(N)]

# ranky=[]
# ranko=[]
# for row in range(N):
# 	for col,each in enumerate(info[row]):
# 		if each=='W':
# 			continue

# 		if each=='Y':
# 			ranky.append((genres[row][col],ratings_dict[genres[row][col]],row,col))
# 		else:
# 			ranko.append((genres[row][col],ratings_dict[genres[row][col]],row,col))


# ranky=sorted(ranky,key=lambda x:x[1],reverse=True)
# ranko=sorted(ranko,key=lambda x:x[1],reverse=True)

# for element in ranky:
# 	for each in element:
# 		print(each, end=" ")
# 	print()

# for element in ranko:
# 	for each in element:
# 		print(each, end=" ")
# 	print()


# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# from collections import deque
# col, row = map(int, input().split())

# path = [list(input())for _ in range(row)]

# ud = [(1,0)]
# lr = [(0,-1), (0, 1)]


# def possible_path(x, y):
#     if x < 0 or x >= row or y < 0 or y >= col:
#         return False
#     else:
#         if visited[x][y] == 1 or path[x][y] == 'x':
#             return False
#         else:
#             return True


# def bfs(startx, starty):
#     visited[startx][starty]=1
#     queue = deque()
#     queue.append((startx, starty, 0))

#     while queue:
#         posx, posy, cnt = queue.popleft()
#         if posx == row-1:
#             cnt_list.append(cnt)
#             continue


#         for udx, udy in ud:
#             nextx = posx+udx
#             nexty = posy+udy
#             if possible_path(nextx, nexty):
#                 queue.append((nextx, nexty, cnt))
#                 visited[nextx][nexty] = 1

#         for lrx, lry in lr:
#             nextx = posx+lrx
#             nexty = posy+lry
#             if possible_path(nextx, nexty):
#                 queue.append((nextx, nexty, cnt+1))
#                 visited[nextx][nexty] = 1

# ans = 0
# cnt_list=[]
# for start, vertex in enumerate(path[0]):
#     visited = [[0]*col for _ in range(row)]
#     if vertex == 'c':
#         bfs(0, start)

# if len(cnt_list)==0:
# 	print(-1)
# else:
# 	print(min(cnt_list))

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque
col, row = map(int, input().split())
clothes = [list(map(int, input().split())) for _ in range(row)]


dir = [(0, 1), (1, 0)]


def possible_path(x, y):
    if x < 0 or x >= row or y < 0 or y >= col:
        return False
    else:
        if visited[x][y] == 1:
            return False
        else:
            return True


def bfs(startx, starty):
    visited[startx][starty] = 1
    queue = deque()
    queue.append((startx, starty, clothes[startx][starty]))

    while queue:
        posx, posy, cnt = queue.popleft()
        if posx == row-1 and posy == col-1:
            cnt_list.append(cnt)
            continue
        for dirx, diry in dir:
            nextx = posx+dirx
            nexty = posy+diry
            if possible_path(nextx, nexty):
                queue.append((nextx, nexty, cnt+clothes[nextx][nexty]))
                if nextx != row-1 and nexty != col-1:
                    visited[nextx][nexty] = 1


visited = [[0]*col for _ in range(row)]
cnt_list = []
bfs(0, 0)
print(max(cnt_list))

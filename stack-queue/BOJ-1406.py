from sys import stdin
from collections import deque
edit=deque(input())

M=int(stdin.readline().rstrip())
left=edit
right=deque()

for i in range(M):
    commands=list(stdin.readline().split())
    # cursor=len(left)
    if commands[0]=="P":
        left.append(commands[1])
        
    elif commands[0]=="L":
        if len(left)>0:
            right.append(left.pop())
    elif commands[0]=="D":
        if len(right)>0:
            left.append(right.pop())
        
    elif commands[0]=="B":
        if len(left)>0:
            left.pop()


print(''.join(left)+''.join(reversed(right)))


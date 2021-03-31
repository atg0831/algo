from sys import stdin
from collections import deque

input=stdin.readline().split()
brackets=deque(input[0])

cnt=0
stack=[]
prev=-1
for bracket in brackets:
    if bracket=="(":
        stack.append(bracket)
    
    else:
        stack.pop()
        if prev=="(":
            cnt+=len(stack)
        else:
            cnt+=1

    prev=bracket

print(cnt)
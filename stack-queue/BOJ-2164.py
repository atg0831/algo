from collections import deque

N=int(input())
queue=deque()

for i in range(1,N+1):
    queue.append(i)

while len(queue)>1:
    top=queue.popleft()
    to_bottom=queue.popleft()
    queue.append(to_bottom)

print(queue[0])
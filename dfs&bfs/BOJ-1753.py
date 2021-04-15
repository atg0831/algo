from collections import deque
import heapq
import sys
V, E = map(int, sys.stdin.readline().rstrip().split())
K = int(input())

graph = [[]for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((v, w))

INF = sys.maxsize
dist = [INF for _ in range(V+1)]


def dijkstra(graph, start):
    dist[start] = 0

    queue = []
    heapq.heappush(queue, (dist[start], start))

    while queue:  
        weight, now = heapq.heappop(queue)
        if dist[now] < weight:
            continue

        for u, w in graph[now]:
            cost = weight + w
            if cost < dist[u]:
                dist[u] = cost
                heapq.heappush(queue, (cost, u))


dijkstra(graph, K)
for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])

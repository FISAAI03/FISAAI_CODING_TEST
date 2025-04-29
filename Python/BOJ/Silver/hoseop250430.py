import sys
import math
INF = math.inf

input = sys.stdin.readline

g = {}

v_cnt, e_cnt = map(int, input().split())
dist = [INF] * (v_cnt+1)

k = int(input())
dist[k] = 0

for _ in range(e_cnt):
    u, v, w = map(int, input().split())
    if u not in g:
        g[u] = {v: w}
    else:
        g[u][v] = w

def dijkstra(k):
    visited = []
    next = {k:1}
    while next:
        min_v = min(next, key=lambda x: dist[x])
        del next[min_v]
        visited.append(min_v)

        if min_v in g:
            for v in g[min_v]:
                dist[v] = min(dist[v], dist[min_v] + g[min_v][v])
                if (v not in next) and (v not in visited):
                    next[v] = 1
    

dijkstra(k)
for d in dist[1:]:
    print('INF') if d==INF else print(d)

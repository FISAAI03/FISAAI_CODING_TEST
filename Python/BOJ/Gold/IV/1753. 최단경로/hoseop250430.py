import sys
import math
from collections import defaultdict

INF = math.inf

input = sys.stdin.readline

g = defaultdict(dict)

v_cnt, e_cnt = map(int, input().split())
# 최단 거리 저장 리스트트
dist = [INF] * (v_cnt+1)

k = int(input())

for _ in range(e_cnt):
    u, v, w = map(int, input().split())
    if v not in g[u] or g[u][v] > w:  # 중복 간선 처리
        g[u][v] = w

# 다익스트라 알고리즘 활용 (가중치가 있는 그래프 최단 경로 알고리즘)
def dijkstra(k):
    # 시작점의 거리 0으로 초기화
    dist[k] = 0
    visited = []
    # 다음 경로의 정점을을 저장하는 리스트 생성
    next = [k]
    while next:
        # next안의 정점들 중 최단 거리의 정점 선택
        min_v = min(next, key=lambda x: dist[x])
        next.remove(min_v)
        visited.append(min_v)

        if min_v in g:
            # min_v 정점 경로의 다음 정점들을 순회
            for v in g[min_v]:
                # 거리 값을 최소인 값으로 dist 업데이트
                dist[v] = min(dist[v], dist[min_v] + g[min_v][v])
                if (v not in next) and (v not in visited):
                    next.append(v)

dijkstra(k)
for d in dist[1:]:
    print('INF') if d==INF else print(d)

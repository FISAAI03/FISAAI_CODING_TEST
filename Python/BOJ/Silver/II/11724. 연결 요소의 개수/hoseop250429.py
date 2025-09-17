import sys
from collections import defaultdict

# bfs 함수로 visited 정점 리턴 (정점 그룹화 목적)
def bfs(start):
    queue = [start]
    visited = [start]

    while queue:
        start = queue.pop(0)
        if start in g:
            for i in g[start]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

    return visited

input = sys.stdin.readline

n, m = map(int, input().split())
# 빠른 정점 찾기를 위한 defaultdict 그래프 생성
g = defaultdict(list) # 딕셔너리의 value 초기값의 타입을 명시(할당)

for _ in range(m):
    u, v = map(int, input().split())
    # 방향 없는 그래프를 위한 양방향 할당
    g[u].append(v)
    g[v].append(u)

cnt = 0

total_visited = []

for i in range(1, n+1):
    if (i not in total_visited):
        # bfs가 한번 실행될때마다 연결 요소가 그룹화됨
        # 그룹화된 visited 정점들을 total_visited에 extend
        total_visited += bfs(i)
        # 연결 요소 그룹화 함수(bfs)가 실행 될때마다 그룹 카운트
        cnt += 1
    
print(cnt)
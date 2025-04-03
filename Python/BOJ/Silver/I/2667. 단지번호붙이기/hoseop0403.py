import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

map = [list(map(int, input().strip())) for _ in range(n)]

# 방문한 집 확인을 위해 지도와 같은 크기의 배열 생성성 
visited = [[False]*n for _ in range(n)]

cplx_cnt = []

# bfs와 cnt 값을 활용하여 풀이이
def bfs(x, y):

    next_step = deque([(x, y)])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited[x][y] = True
    cnt = 1

    while next_step:
        x, y = next_step.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if (map[nx][ny] == 1) and (visited[nx][ny] == False):
                    next_step.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt

# 모든 지도를 돌며 방문 했는지 확인 후 메모리 최적화 하여 값 저장장
for x in range(n):
    for y in range(n):
        if (map[x][y] == 1) and (visited[x][y] == False):
            cplx_cnt.append(bfs(x, y))

cplx_cnt.sort()
print(len(cplx_cnt))
for c in cplx_cnt:
    print(c)
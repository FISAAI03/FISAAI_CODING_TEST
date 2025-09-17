import sys
from collections import deque

'''
visited 차원을 3개로 하여 
visited[x][y][0] 차원에서는 벽을 안부순 경우의 방문 노드
visited[x][y][1] 차원   에서는 벽을 부순 경우의 방문 노드
총 x * y * 2 만큼의 경우의 수를 설정
벽을 안부수고의 경로와 벽을 부수고 나서의 경로가 '겹치지 않도록' 2개의 차원으로 분할하여 경로를 탐색
=> queue에 노드가 [x][y][0]차원과 [x][y][1]차원으로 구성되어 2배로 쌓이기에 메모리가 많이 든다.
=> 내가 이전에 냈던 메모리 초과 코드랑 뭐가 다른건지 모르겠음.
'''

def bfs(x, y):
    queue = deque([(x, y, 1, 0)])
    visited[x][y][0] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y, dist, broken = queue.popleft()
        if x == n-1 and y == m-1:
            return dist

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if map[nx][ny] == 0 and not visited[nx][ny][broken]:
                    queue.append((nx, ny, dist+1, broken))
                    visited[nx][ny][broken] = True
                    
                elif (map[nx][ny] == 1) and (broken == 0) and not visited[nx][ny][1]:
                    queue.append((nx, ny, dist+1, 1))
                    visited[nx][ny][1] = True
                    

input = sys.stdin.readline

n, m = map(int, input().split())

map = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[False]*2  for _ in range(m)] for _ in range(n)]

ans = bfs(0, 0)
print(ans) if ans else print(-1)
from collections import deque
import sys

# bfs함수를 통해 배추가 이어진 곳을 확인 및 visited를 갱신해줌
def bfs(y, x):
    queue = deque([[y, x]])
    visited[y][x] = True
    while queue:
        cur_y, cur_x = queue.popleft()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(4):
            ny, nx = cur_y+dy[i], cur_x+dx[i]
            if (0 <= nx < m) and (0 <= ny < n) and (grid[ny][nx] == 1):
                if not visited[ny][nx]:
                    queue.append([ny, nx])
                    visited[ny][nx] = True
    

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == 1) and (visited[i][j] == False):
                # bfs가 한번 실행되면 배추가 이어진 곳이 그룹화 되어 count를 +1해줌
                bfs(i, j)
                cnt += 1
    print(cnt)
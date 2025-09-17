import sys
from collections import deque

n, m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]

# 너비 우선 탐색 활용
def bfs(x, y):
    # 덱에 시작점 저장
    next_step = deque()
    next_step.append((x, y))
    
    # 상, 하, 좌, 우 리스트 생성
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 다음 단계 없을 때까지 queue를 활용하여 미로 탐색
    while next_step:
        x, y = next_step.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 미로 범위 안에서 탐색
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                # 갈 수 있는 방향(1) 인지 확인
                if maze[nx][ny] == 1:
                    # 다음 단계의 좌표를 next_step에 저장
                    next_step.append((nx, ny))
                    # 한 단계 이동할 때마다 이동 거리(1)를 더해서 갱신
                    maze[nx][ny] = maze[x][y] + 1
    
bfs(0, 0)

print(maze[n-1][m-1])


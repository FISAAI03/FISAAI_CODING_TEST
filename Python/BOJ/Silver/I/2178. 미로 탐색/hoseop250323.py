import sys
from collections import deque

# input = sys.stdin.readline()
n, m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]
print(maze)

def bfs(x, y):
    next_step = deque()
    next_step.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while next_step:
        x, y = next_step.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if maze[nx][ny] == 1:
                    next_step.append((nx, ny))
                    maze[nx][ny] = maze[x][y] + 1
    
bfs(0, 0)

print(maze[n-1][m-1])


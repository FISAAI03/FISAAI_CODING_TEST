from collections import deque
import sys

def bfs(x, y, gx, gy):
    queue = deque([(x, y, 0)])
    visited = [[False]*l for _ in range(l)]
    visited[x][y] = True
    direct = [(-2, 1), (-2, -1), (-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2)]

    while queue:
        x, y, cnt = queue.popleft()
        if x == gx and y == gy:
            return cnt
        for dx, dy in direct:
            nx, ny = x+dx, y+dy
            if 0 <= nx < l and 0 <= ny < l:
                if not visited[nx][ny]:
                    queue.append((nx, ny, cnt+1))
                    visited[nx][ny] = True

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    l = int(input())
    start_x, start_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    print(bfs(start_x, start_y, goal_x, goal_y))

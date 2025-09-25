# 15:15 ~ 15:40

import sys
from collections import deque

input = sys.stdin.readline

# 0,0 -> n-1, m-1
n, m = map(int, input().split())
adj = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

move_y = [1, 0, -1, 0]
move_x = [0, 1, 0, -1]

def check_outline(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    return False

def dfs(s_y, s_x):
    answer = []
    q = deque()
    q.append([s_y, s_x, 1])
    visited[s_y][s_x] = 1

    while len(q) > 0:
        c_y, c_x, count = q.popleft()
        if c_y == n - 1 and c_x == m - 1:
            answer.append(count)
        for idx in range(4):
            if check_outline(c_y + move_y[idx], c_x + move_x[idx]):
                if adj[c_y + move_y[idx]][c_x + move_x[idx]] == '1' and visited[c_y + move_y[idx]][c_x + move_x[idx]] == 0:
                    q.append([c_y + move_y[idx], c_x + move_x[idx], count + 1])
                    visited[c_y + move_y[idx]][c_x + move_x[idx]] = 1
    
    return min(answer)

t = dfs(0, 0)
print(t)
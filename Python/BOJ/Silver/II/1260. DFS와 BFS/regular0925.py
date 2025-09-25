# 14:02 ~ 14:28

import sys

sys.setrecursionlimit(100_000)
input = sys.stdin.readline

# Setting
n, m, s = input().split()
n = int(n)
m = int(m)
s = int(s)

adj = [[0] * (n+1) for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = input().split()
    adj[int(a)][int(b)] = 1
    adj[int(b)][int(a)] = 1

# dfs
answer = []

def dfs(s):
    answer.append(str(s))
    visited[s] = 1
    for idx in range(n + 1):
        if adj[s][idx] == 1 and visited[idx] == 0:
            dfs(idx)

dfs(s)
print(' '.join(answer))

# bfs
from collections import deque

answer = []
visited = [0] * (n + 1)
def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while len(q) > 0:
        cur =  q.popleft()
        
        answer.append(str(cur))
        for idx in range(n + 1):
            if adj[cur][idx] == 1 and visited[idx] == 0:
                visited[idx] = 1
                q.append(idx)

bfs(s)
print(' '.join(answer))
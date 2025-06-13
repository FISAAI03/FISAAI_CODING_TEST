import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

box = []
cnt_0 = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    cnt_0 += tmp.count(0)
    box.append(tmp)

def bfs():
    queue = deque([])
    # 초기에 토마토가 심어진 곳(1)의 위치를 찾아서 queue에 삽입
    # -> 하루하루 동시에 토마토가 익을 수 있음
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j, 0))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 남아 있는 0개수와 익은 토마토 개수 비교를 위한 cnt 선언
    cnt = 0
    # 최소 날짜를 반환하기 위한 min_day 글로벌 변수로 선언
    global min_day
    min_day = 0

    while queue:
        x, y, day = queue.popleft()
        min_day = day
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<m and box[nx][ny] == 0:
                box[nx][ny] = 1
                queue.append((nx, ny, day+1))
                cnt += 1
    
    return min_day, cnt

day, cnt = bfs()

# 0의 개수와 익은 토마토의 개수가 같다면, 모든 토마토가 익었음을 알 수 있음
if cnt == cnt_0:
    print(day)
else:
    print(-1)

            
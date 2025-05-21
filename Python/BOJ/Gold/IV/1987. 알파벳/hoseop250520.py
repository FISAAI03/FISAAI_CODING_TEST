import sys


# 백트래킹 재귀 함수를 활용한 경로 탐색 방법
def dfs(x, y, alpha):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 재귀 함수에서도 변화를 확인하기 위한 전역 변수 설정
    global mx_cnt
    mx_cnt = max(len(alpha), mx_cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] not in alpha:
                alpha.add(board[nx][ny])
                dfs(nx, ny, alpha)
                alpha.remove(board[nx][ny]) # 백트래킹

input = sys.stdin.readline

r, c = map(int, input().split())

board = [list(input().strip()) for _ in range(r)]
alpha = set([board[0][0]])
mx_cnt = 1

dfs(0, 0, alpha)

print(mx_cnt)

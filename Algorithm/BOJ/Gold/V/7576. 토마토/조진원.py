from collections import deque

# M: 열(가로) 개수, N: 행(세로) 개수 입력
M, N = map(int, input().split())

# 보드(토마토 상태) 입력 받기
# 1: 익은 토마토, 0: 안 익은 토마토, -1: 빈 칸
board = [list(map(int, input().split())) for _ in range(N)]

def solution(M, N, board):
    # 방문 여부를 저장하는 2차원 리스트 초기화
    chk = [[False for _ in range(M)] for _ in range(N)]

    # BFS를 위한 큐 생성
    queue = deque([])

    # 보드를 순회하며 초기 상태 설정
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:  # 익은 토마토인 경우
                queue.append((i, j, 0))  # 위치와 시작일(0일차)을 큐에 추가
                chk[i][j] = True  # 방문 처리
            elif board[i][j] == -1:  # 빈 칸인 경우
                chk[i][j] = True  # 방문 처리 (익힐 필요 없음)

    # 방향 벡터 설정 (상, 하, 좌, 우)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    max_day = 0  # 모든 토마토가 익는 데 걸리는 최대 일 수

    # BFS 시작
    while queue:
        x, y, d = queue.popleft()  # 현재 위치(x, y)와 날짜(d)를 꺼냄
        max_day = max(max_day, d)  # 현재까지의 최대 날짜 갱신

        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 안에 있고, 아직 방문하지 않았으며 익힐 수 있는 토마토인 경우
            if (0 <= nx < N) and (0 <= ny < M) and chk[nx][ny] == False:
                queue.append((nx, ny, d + 1))  # 다음 날에 익음
                chk[nx][ny] = True  # 방문 처리

    # BFS 종료 후, 안 익은 토마토가 남아 있는지 확인
    for i in range(N):
        for j in range(M):
            if chk[i][j] == False:
                return -1  # 아직 익지 않은 토마토가 있다면 -1 반환

    return max_day  # 모든 토마토가 익는 데 걸린 일 수 반환

# 결과 출력
print(solution(M, N, board))
from collections import deque
import copy

# 너비 우선 탐색 (BFS) 함수
def bfs(queue, chk, target, maps):
    row = len(maps)   # 행 길이
    col = len(maps[0])  # 열 길이

    # 상하좌우 이동 방향
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y, d = queue.popleft()  # 현재 위치 (x, y)와 이동 거리 d

        # 목표 지점에 도달하면 거리 반환
        if maps[x][y] == target:
            return d

        # 네 방향 탐색
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위 내이고 방문하지 않은 통로라면
            if 0 <= nx < row and 0 <= ny < col and chk[nx][ny] == False:
                chk[nx][ny] = True  # 방문 처리
                queue.append((nx, ny, d + 1))  # 거리 1 증가

    return -1  # 목표에 도달할 수 없는 경우

# 전체 풀이 함수
def solution(maps):
    row = len(maps)        # 행 수
    col = len(maps[0])     # 열 수

    # 벽 정보를 기반으로 방문 여부 배열 생성
    origin_chk = [[False for _ in range(col)] for _ in range(row)]

    # 시작점(S), 레버(L) 위치와 벽(X) 체크
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 'X':
                origin_chk[i][j] = True  # 벽은 방문 불가
            elif maps[i][j] == 'S':
                sx = i
                sy = j
            elif maps[i][j] == 'L':
                lx = i
                ly = j

    # 1단계: 시작점 → 레버까지 거리 구하기
    l_chk = copy.deepcopy(origin_chk)  # 방문 체크 배열 복사
    l_chk[sx][sy] = True  # 시작점 방문 처리
    l_queue = deque([(sx, sy, 0)])  # 시작점에서 BFS 시작
    l_dist = bfs(l_queue, l_chk, 'L', maps)  # 레버까지 거리 계산

    if l_dist == -1:
        return -1  # 레버에 도달할 수 없으면 실패

    # 2단계: 레버 → 출구까지 거리 구하기
    e_chk = copy.deepcopy(origin_chk)  # 방문 체크 배열 다시 복사
    e_chk[lx][ly] = True  # 레버 위치 방문 처리
    e_queue = deque([(lx, ly, 0)])  # 레버에서 BFS 시작
    e_dist = bfs(e_queue, e_chk, 'E', maps)  # 출구까지 거리 계산

    if e_dist == -1:
        return -1  # 출구에 도달할 수 없으면 실패

    # 총 거리 = 시작점 → 레버 거리 + 레버 → 출구 거리
    return l_dist + e_dist

from collections import deque

def solution(board):
    
    lenx = len(board)     # 보드의 세로 길이
    leny = len(board[0])  # 보드의 가로 길이
    queue = deque([])     # BFS쓸 큐 생성
    
    # 방문 여부를 체크할 배열
    chk = [[False for _ in range(leny)] for _ in range(lenx)]
    
    # 초기 맵 설정
    maps = [[0 for _ in range(leny)] for _ in range(lenx)]
    
    # 보드를 순회하면서 시작점(R), 목표점(G), 장애물(D)을 설정
    for i in range(lenx):
        for j in range(leny):
            if board[i][j] == 'D':   # 장애물
                maps[i][j] = 'D'
                chk[i][j] = True     # 방문 불가로 설정
            elif board[i][j] == 'R': # 시작점
                maps[i][j] = 'R'
                queue.append((i, j, 0))  # 좌표와 이동 횟수를 큐에 저장
                chk[i][j] = True
            elif board[i][j] == 'G': # 목표점
                maps[i][j] = 'G'
    
    # 방향 배열
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    # BFS 시작
    while queue:
        x, y, d = queue.popleft()  # 현재 좌표와 이동 횟수
        
        # 목표점에 도착하면 이동 횟수 반환
        if maps[x][y] == 'G':
            return d
        
        # 4방향으로 탐색
        for nx, ny in zip(dx, dy):
            cx, cy = x, y
            
            # 미끄러지기
            while 0 <= (cx + nx) < lenx and 0 <= (cy + ny) < leny and maps[cx + nx][cy + ny] != 'D':
                cx += nx
                cy += ny
            
            # 도착한 위치가 아직 방문하지 않은 곳이면 큐에 추가
            if chk[cx][cy] == False:
                chk[cx][cy] = True
                queue.append((cx, cy, d + 1))
    
    # 목표점에 도달할 수 없는 경우 -1 반환
    return -1

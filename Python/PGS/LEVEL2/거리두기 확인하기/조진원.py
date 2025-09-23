from collections import deque

def chk_bfs(maps) :
    # 방문 여부를 기록할 배열 (5x5)
    chk = [[False for _ in range(5)] for _ in range(5)]
    
    # 상, 우, 하, 좌 이동 방향
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    # 사람(P)의 좌표를 담을 리스트
    p_point = []
    for x in range(5) :
        for y in range(5) :
            if maps[x][y] == 'P' :
                # 사람 위치 저장
                p_point.append((x,y))
                
            elif maps[x][y] == 'X' :
                # 파티션(X)은 방문 불가능 처리
                chk[x][y] = True
    
    # 사람이 한 명도 없으면 조건 위반 없음 → 통과
    if not p_point :
        return 1
    
    # 각 사람 좌표별로 BFS 수행
    for px, py in p_point :
        # 공용 chk 배열을 복사해서 사용 (깊이 제한 BFS 전용)
        sub_chk = chk.copy()
        # 시작점 방문 처리
        sub_chk[px][py] = True
        # (좌표, 거리) 큐 초기화
        queue = deque([(px,py,0)])
        
        while queue :
            x, y, d = queue.popleft()
            
            # 4방향 탐색
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 5x5 범위 안, 아직 방문 X, 거리 2 이하일 때만 탐색
                if (0<=nx<5) and (0<=ny<5) and (not sub_chk[nx][ny]) and d+1 < 3 :
                    if maps[nx][ny] == 'P' :
                        # 다른 사람(P)을 발견하면 거리두기 위반
                        return 0
                    else :
                        # 빈 공간(O)이면 계속 탐색
                        sub_chk[nx][ny] = True
                        queue.append((nx,ny,d+1))
                        
    # 모든 탐색에서 문제 없으면 거리두기 지킴
    return 1
                

def solution(places):
    answer = []
    
    # 각 대기실에 대해 검사 결과 추가
    for maps in places :
        answer.append(chk_bfs(maps))
    return answer

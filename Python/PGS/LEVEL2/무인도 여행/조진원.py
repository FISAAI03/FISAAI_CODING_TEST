def solution(maps):
    H = len(maps)      # 행
    W = len(maps[0])   # 열
    
    # 방문 여부 체크
    chk = [[False for _ in range(W)] for _ in range(H)]
    
    # 바다인 칸은 방문 처리
    for i in range(H):
        for j in range(W):
            if maps[i][j] == 'X':
                chk[i][j] = True
                
    answer = []   
    
    # 상, 하, 좌, 우 탐색
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    # 모든 칸을 순회하면서 섬 탐색 시작
    for i in range(H):
        for j in range(W):
            if chk[i][j]:   # 이미 방문했거나 바다라면 건너뜀
                continue
            
            # DFS탐색
            stack = [(i, j)]
            chk[i][j] = True
            s = int(maps[i][j])   # 해당 섬의 식량 합
            
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    # 지도 범위 안에 있고, 아직 방문하지 않은 육지라면
                    if 0 <= nx < H and 0 <= ny < W and not chk[nx][ny]:
                        chk[nx][ny] = True                # 방문 체크
                        s += int(maps[nx][ny])            # 식량 추가
                        stack.append((nx, ny))            # 다음 탐색 좌표로 추가
            
            # 하나의 섬 탐색이 끝났다면 결과 리스트에 추가
            answer.append(s)
    
    # 섬이 하나도 없는 경우 [-1] 반환
    if not answer:
        return [-1]
    else:
        return sorted(answer)   # 오름차순 정렬 후 반환

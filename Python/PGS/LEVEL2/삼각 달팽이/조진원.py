def solution(n):
    # 1. 삼각형 형태의 2차원 리스트(board)를 생성
    board = []
    for i in range(1, n+1):
        bod = [0 for _ in range(i)]  # 각 행은 길이가 점점 늘어남 (1, 2, 3, ..., n)
        board.append(bod)

    # 2. 이동 방향 설정 (↓ → ↖ 순으로 회전)
    dx = [1, 0, -1]  # x축 방향 이동: 아래, 오른쪽, 위쪽(좌상단)
    dy = [0, 1, -1]  # y축 방향 이동

    # 3. 채워야 할 숫자의 개수는 1부터 n까지의 합: n(n+1)/2
    k = n * (n + 1) // 2

    # 4. 시작 위치와 방향
    x = 0
    y = 0
    d = 0  # 현재 방향 인덱스 (0: 아래, 1: 오른쪽, 2: 좌상단)

    # 5. 1부터 k까지 숫자를 채움
    for i in range(1, k + 1):
        board[x][y] = i  # 현재 위치에 숫자 채우기

        if i == k:  # 마지막 숫자라면 더 이상 이동하지 않고 종료
            continue

        # 6. 다음 위치가 유효할 때까지 방향을 바꿔가며 탐색
        while True:
            # 다음 위치 계산
            nx = x + dx[d]
            ny = y + dy[d]

            # 다음 위치가 범위 내에 있고 아직 채워지지 않았다면 이동
            if 0 <= nx < len(board) and 0 <= ny < len(board[nx]) and board[nx][ny] == 0:
                x = nx
                y = ny
                break  # 이동했으면 반복 종료
            else:
                d = (d + 1) % 3  # 방향 전환 (0 → 1 → 2 → 0)

    # 7. 이중 리스트를 평탄화하여 1차원 리스트로 반환
    return sum(board, [])

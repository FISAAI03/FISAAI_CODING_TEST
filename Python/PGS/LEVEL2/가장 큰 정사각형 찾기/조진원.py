'''핵시 풀이방법은 DP'''

def solution(board):
    
    # 행과 열 숫자 뽑기
    col = len(board[0])
    row = len(board)
    
    # 체크배열 만들기
    chk = [[0 for _ in range(col)] for _ in range(row)]

    # 초기값 설정
    biggest = 0
    for i in range(row):
        for j in range(col):
            # 행과 열이 0 부분은 본래 표에 것을 그대로 따른다.
            if i == 0 or j == 0: 
                chk[i][j] = board[i][j]
                
            # 기존 표에서 1인 부분만 갱신, 0인부분은 정사각형이 되지 않음
            elif board[i][j] == 1:
                # 현재 위치에서 만들 수 있는 가장 큰 정사각형의 한 변의 길이를 계산합니다
                # 이 값은 현재 위치의 왼쪽, 위쪽, 왼쪽 위 대각선 방향의 값 중 최소값에 1을 더한 것
                # 1. 왼쪽, 위쪽, 왼쪽 위 대각선 방향이 모두 1 이상이어야 정사각형을 확장할 수 있음
                # 2. 이 중 가장 작은 값이 현재 위치에서 만들 수 있는 정사각형의 한계를 결정
                # 3. 여기에 1을 더함으로써 현재 위치를 포함한 새로운 정사각형의 크기를 구함
                chk[i][j] = min(chk[i-1][j], chk[i][j-1], chk[i-1][j-1]) + 1
                
                # 그리고 최대 크기 갱신
                biggest = max(biggest, chk[i][j]) 
            
    return biggest ** 2 # 넓이를 구하는 것이니 제곱
def solution(rows, columns, queries):
    
    matrix = [[i*columns + (j+1) for j in range(columns)] for i in range(rows)]
    
    result = []
    
    
    for [sx, sy, ex, ey] in queries :
        
        sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1
        
        # 초기값 설정
        prev = matrix[sx][sy]
        min_val = prev

        # 시계방향 돌면서 바꾸기
        # 위쪽 행 (좌→우)
        for y in range(sy+1, ey+1):
            matrix[sx][y], prev = prev, matrix[sx][y]
            min_val = min(min_val, prev)

        # 오른쪽 열 (위→아래)
        for x in range(sx+1, ex+1):
            matrix[x][ey], prev = prev, matrix[x][ey]
            min_val = min(min_val, prev)

        # 아래쪽 행 (우→좌)
        for y in range(ey-1, sy-1, -1):
            matrix[ex][y], prev = prev, matrix[ex][y]
            min_val = min(min_val, prev)

        # 왼쪽 열 (아래→위)
        for x in range(ex-1, sx-1, -1):
            matrix[x][sy], prev = prev, matrix[x][sy]
            min_val = min(min_val, prev)

        result.append(min_val)
        
    return result
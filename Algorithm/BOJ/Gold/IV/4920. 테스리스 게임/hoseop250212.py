import sys

ans = []
n = int(sys.stdin.readline())

while n!=0:

    maxx = -4000000
    block = []

    for _ in range(n):
        block.append(list(map(int, sys.stdin.readline().split())))
    
    
    # 1. 막대
    ## 가로
    for col in range(n):
        for row in range(n-3):
            summ = sum(block[col][row: row+4])
            if maxx < summ:
                maxx = summ
    ## 세로
    for col in range(n-3):
        for row in range(n):
            summ = block[col][row] + block[col+1][row] + block[col+2][row] + block[col+3][row]
            if maxx < summ:
                maxx = summ
    # 2. 정사각형
    for col in range(n-1):
        for row in range(n-1):
            summ = sum(block[col][row: row+2]) + sum(block[col+1][row: row+2])
            if maxx < summ:
                maxx = summ
    # 3. 나머지 3개
    # 가로
    for col in range(n-1):
        for row in range(n-2):
            # ㄱㄴ
            summ1 = sum(block[col][row: row+2]) + sum(block[col+1][row+1: row+3])
            # ㄱ
            summ2 = sum(block[col][row: row+3]) + block[col+1][row+2]
            # ㄴ
            summ3 = block[col][row] + sum(block[col+1][row: row+3])
            # ㅜ
            summ4 = sum(block[col][row: row+3]) + block[col+1][row+1]
            # ㅗ
            summ5 = block[col][row+1] + sum(block[col+1][row: row+3])
            if maxx < max([summ1, summ2, summ3, summ4, summ5]):
                maxx = max([summ1, summ2, summ3, summ4, summ5])
    # 세로
    for col in range(n-2):
        for row in range(n-1):
            # ㄱㄴ 90도 회전
            summ1 = block[col][row+1] + sum(block[col+1][row: row+2]) + block[col+2][row]
            # ㄱ 90도 회전
            summ2 = block[col][row+1] + block[col+1][row+1] + sum(block[col+2][row: row+2])
            # ㄴ 90도 회전
            summ3 = sum(block[col][row: row+2]) + block[col+1][row] + block[col+2][row]
            # ㅓ
            summ4 = block[col][row+1] + sum(block[col+1][row: row+2]) + block[col+2][row+1]
            # ㅏ
            summ5 = block[col][row] + sum(block[col+1][row: row+2]) + block[col+2][row]
            if maxx < max([summ1, summ2, summ3, summ4, summ5]):
                maxx = max([summ1, summ2, summ3, summ4, summ5])
    ans.append(maxx)
    n = int(sys.stdin.readline())

for i in range(len(ans)):
    print(f'{i+1}. {ans[i]}')
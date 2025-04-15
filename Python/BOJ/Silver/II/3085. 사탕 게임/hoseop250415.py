import sys
import copy

input = sys.stdin.readline

n = int(input())

board = [list(input().strip()) for _ in range(n)]

mx_cnt = 0

for r in range(n):
    cnt = 1
    for c in range(n-1):
        if board[r][c] == board[r][c+1]:
            cnt += 1
        else:
            if mx_cnt < cnt :
                mx_cnt = cnt
            cnt = 1
    if mx_cnt < cnt :
        mx_cnt = cnt

for c in range(n):
    cnt = 1
    for r in range(n-1):
        if board[r][c] == board[r+1][c]:
            cnt += 1
        else:
            if mx_cnt < cnt:
                mx_cnt = cnt
            cnt = 1
    if mx_cnt < cnt :
        mx_cnt = cnt


for i in range(n):
    for j in range(n):
        if j < n-1:
            tmp = copy.deepcopy(board)
            if tmp[i][j] != tmp[i][j+1]:
                tmp[i][j], tmp[i][j+1] = tmp[i][j+1], tmp[i][j]

                cnt = 1
                for col in range(n-1):
                    if tmp[i][col] == tmp[i][col+1]:
                        cnt += 1
                    else:
                        if mx_cnt < cnt :
                            mx_cnt = cnt
                        cnt = 1
                if mx_cnt < cnt :
                    mx_cnt = cnt

                cnt = 1
                for row in range(n-1):
                    if tmp[row][j] == tmp[row+1][j]:
                        cnt += 1
                    else:
                        if mx_cnt < cnt:
                            mx_cnt = cnt
                        cnt = 1
                if mx_cnt < cnt :
                    mx_cnt = cnt

                cnt = 1
                for row in range(n-1):
                    if tmp[row][j+1] == tmp[row+1][j+1]:
                        cnt += 1
                    else:
                        if mx_cnt < cnt:
                            mx_cnt = cnt
                        cnt = 1
                if mx_cnt < cnt :
                    mx_cnt = cnt

        if i < n-1:
            tmp1 = copy.deepcopy(board)
            if tmp1[i][j] != tmp1[i+1][j]:
                tmp1[i][j], tmp1[i+1][j] = tmp1[i+1][j], tmp1[i][j]

                cnt = 1
                for row in range(n-1):
                    if tmp1[row][j] == tmp1[row+1][j]:
                        cnt += 1
                    else:
                        if mx_cnt < cnt:
                            mx_cnt = cnt
                        cnt = 1
                if mx_cnt < cnt :
                    mx_cnt = cnt

                cnt = 1
                for col in range(n-1):
                    if tmp1[i][col] == tmp1[i][col+1]:
                        cnt += 1
                    else:
                        if mx_cnt < cnt :
                            mx_cnt = cnt
                        cnt = 1
                if mx_cnt < cnt :
                    mx_cnt = cnt

                cnt = 1
                for col in range(n-1):
                    if tmp1[i+1][col] == tmp1[i+1][col+1]:
                        cnt += 1
                    else:
                        if mx_cnt < cnt :
                            mx_cnt = cnt
                        cnt = 1
                if mx_cnt < cnt :
                    mx_cnt = cnt

print(mx_cnt)
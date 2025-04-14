board = input()

ans = ''
i = 0
while i < len(board):
    if board[i] == '.':
        ans += '.'
        i += 1
    else:
        cnt = 0
        a_cnt = 0
        b_cnt = 0
        # 연속적인 X를 만날 경우 따로 while문으로 처리
        while (i < len(board)) and (board[i] == 'X'):
            cnt += 1
            i += 1
        # 'AAAA' 개수와 'BB'의 개수를 연속적인 X 길이의 몫과 나머지로 할당하여 ans에 붙임
        if cnt % 2 != 0:
            ans = -1
            break
        else:
            a_cnt = cnt // 4
            if cnt % 4 == 2:
                b_cnt = 1
        ans += ('AAAA'*a_cnt) + ('BB'*b_cnt)

print(ans)
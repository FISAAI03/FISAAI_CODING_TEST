# PyPy3코드로 제출해야 시간 초과가 안뜨는 코드입니다. (왜 그런지 모름)
# 인덱스 값(x,y)을 관우, 철원의 실현가능한 효용 값으로 간주하여 생각의 전환을 통해 푼 문제

import sys

n = int(sys.stdin.readline())
# 햄버거 효용값 저장
burger = list(map(int, sys.stdin.readline().split()))
sum = sum(burger)
# 관우와 철환이의 각각의 효용값을 저장할 2차원 dynamic programing 리스트 생성
dp = [[0] * (sum+1) for _ in range(sum+1)]
total = 0

dp[0][0] = 1

# i = 저장된 햄버거 효용값 인덱스, x = 관우가 먹을 수 있는 모든 경우의 햄버거 효용값을 인덱스로 표현, y = 철원이 먹을 수 있는 모든 경우의 햄버거 효용값을 인덱스로 표현
# burger 리스트를 돌면서 total값을 이용해 효용값(x, y)의 경우가 존재할 때(dp[x][y]==1), 인덱스에 현재효용값(burger[i])을 더해 해당 인덱스 값을 1로 설정하여 효용값 case 존재 표시
for i in range(n):
    total += burger[i]

    # 현재 햄버거(total)로 만들 수 있는 모든 경우의 수 탐색
    for x in range(total, -1, -1):
        for y in range(total, -1, -1):
            if dp[x][y]==1:
                dp[x+burger[i]][y] = 1
                dp[x][y+burger[i]] = 1

max_gilwon = 0

# 모든 관우, 철원 효용값 경우의 수를 탐색하며 max_gilwon의 최대값을 sum - i - j를 활용하여 찾음
for i in range(1, sum+1):
    for j in range(1, sum+1):
        if dp[i][j]==1:
            min_gilwon = min(sum - i - j, min(i, j))
            max_gilwon = max(min_gilwon, max_gilwon)

print(max_gilwon)
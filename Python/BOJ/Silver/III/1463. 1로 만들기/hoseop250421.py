n = int(input())

# n만큼 인덱스 값 생성
dp = [0] * (n+1)

# dp를 돌면서 최적의 값 선택
for i in range(2, n+1):
    if (i % 3 == 0) and (i % 2 == 0):
        dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i//3], dp[i-1]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i//2], dp[i-1]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[n])
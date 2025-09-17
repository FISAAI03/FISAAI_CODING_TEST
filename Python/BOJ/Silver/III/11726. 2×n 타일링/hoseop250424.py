n = int(input())

# dp = [0]*(n+1)
# dp[0] = 1
# dp[1] = 1
# dp[2] = dp[0] + dp[1]
# dp[3] = d[1] + dp[2]
# dp[4] = dp[2] + dp[3]
# dp[5] = dp[3] + dp[4]
# dp[6] = dp[4] + dp[5]
# dp[7] = dp[5] + dp[6]
# dp[8] = dp[6] + dp[7]
# dp[9] = dp[7] + dp[8]

# if n == 1:
#     print(dp[n])
# else:
#     for i in range(2, n+1):
#         dp[i] = dp[i-2] + dp[i-1]

#     print(dp[n]%10007)

# 피포나치 수열
n0 = 1
n1 = 1
if n == 1:
    print(n0)
else:
    for _ in range(2, n+1):
        n2 = n0 + n1
        n0, n1 = n1, n2
    print(n2%10007)
import sys

input = sys.stdin.readline
N = int(input())
dp = {0: 0, 1: 1}

def fibo(num):
    if num == 0:
        return dp[0]
    if num == 1:
        return dp[1]
    if num in dp.keys():
        return dp[num]
    else:
        dp[num] = fibo(num - 1) + fibo (num - 2)
    return dp[num]

answer = fibo(N)
print(answer)
# 모르겠음 이 문제는.. 뺏김
def solve_towers_4(n):
    """
    Solve the Tower of Hanoi problem with 4 pegs using iteration.

    Parameters:
    n (int): Number of disks to move.

    Returns:
    list: A list containing the minimum number of moves for each number of disks from 0 to n.
    """
    dp = [0] * (n + 1)
    dp[0] = 0
    if n > 0:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = float('inf')
        for k in range(1, i):
            dp[i] = min(dp[i], 2 * dp[k] + (2**(i - k)) - 1)

    return dp

import sys

input = sys.stdin.readline

tc = 1
while 1:
    try:
        n = int(input())
        dp = solve_towers_4(n)
        print(f'Case {tc}: {dp[n]}')
        tc += 1
    except:
        break
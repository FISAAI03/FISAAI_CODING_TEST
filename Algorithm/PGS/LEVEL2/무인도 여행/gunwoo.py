def solution(people, amount):
    donations = [1000, 5000, 10000]
    dp = [[-1] * (amount + 1) for _ in range(people + 1)]
    dp[0][0] = {1000: 0, 5000: 0, 10000: 0}

    for i in range(1, people + 1):
        for j in range(amount + 1):
            for donation in donations:
                if j >= donation and dp[i - 1][j - donation] != -1:
                    dp[i][j] = dp[i - 1][j - donation].copy()
                    dp[i][j][donation] += 1
                    break
    return f"1000원 : {dp[people][amount][1000]}명, 5000원 : {dp[people][amount][5000]}명, 10000원 : {dp[people][amount][10000]}명"

solution(9,22000)
def solution(n):
    MOD = 1000000007

    if n == 1:  # n이 1인 경우
        return 1  # 1을 반환
    elif n == 2:  # n이 2인 경우
        return 2  # 2를 반환
    else:  # n이 1도 2도 아닌 경우
        a, b = 1, 2  # 초기 값 설정, a는 첫 번째 값, b는 두 번째 값
        for i in range(3, n + 1):  # 3부터 n까지 반복
            a, b = b, (a + b) % MOD  # a는 이전 b값을, b는 (이전 a값 + 이전 b값) % MOD 값을 가짐
        return b  # n번째 값을 반환

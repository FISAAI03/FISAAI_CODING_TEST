def solution(n, k):
    if n < 10:
        return n*12000 + k*2000
    elif n >= 10:
        if k > n //10:  # 시킨 음료수(k) > 무료 음료수(n//10)
            return n*12000 + k*2000 - n // 10 * 2000  
        elif k <= n //10:  # 시킨 음료수(k) <= 무료 음료수(n//10)
            return n*12000
    


# 다른 풀이
def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)


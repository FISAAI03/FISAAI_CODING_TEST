def prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num: 
        if num % i == 0:
            return False
        i += 1
    return True

def solution(n):
    answer = 0
    i = 1 
    while i <= n:
        if prime(i): 
            answer += 1
        i += 1 
    return answer

# 시간초과 나는 반쪽짜리 정답

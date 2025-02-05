def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n%i == 0:
            answer += i
        else :
            answer += 0
    return answer

"""
제너레이터 표현식

def solution(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)

# 제너레이터 표현식 연습 예제 : https://chodang-corn.tistory.com/15
"""

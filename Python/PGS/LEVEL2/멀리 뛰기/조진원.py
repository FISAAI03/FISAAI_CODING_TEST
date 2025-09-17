from math import factorial

def count_factorial(a,b) :
    answer = factorial(a+b) // (factorial(a) * factorial(b))
    return answer

def solution(n):
    answer = 0
    # 완전탐색
    two = n // 2
    while two >= 0:
        one = n - two * 2
        answer += count_factorial(one,two)
        two -= 1
    return answer % 1234567
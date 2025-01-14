def solution(a, b, n):
    answer = 0
    while n >= a:
        ex = n//a*b
        answer += ex
        n = ex + n%a
    return answer

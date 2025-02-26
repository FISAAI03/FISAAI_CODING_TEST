import math

def solution(n, m):
    answer = []
    a = n
    b = m
    while b:
        a, b = b, a % b
    answer.append(a)
    answer.append(n*m//a)
    
    return answer
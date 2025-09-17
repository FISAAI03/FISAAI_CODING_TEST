# 소수인지 아닌지 판별
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 진법 변환
def convert(n, base) :
    answer = ''
    if base == 10 :
        return str(n)
    else :
        while n > 0 :
            answer = str(n%base) + answer
            n = n // base
        return answer
    
def solution(n, k):
    answer = 0
    
    # 숫자 변환
    num = convert(n,k)
    
    # 탐색 시작
    for i in num.split('0') :
        if len(i) > 0 :
            if is_prime(int(i)) :
                answer += 1
        
    return answer
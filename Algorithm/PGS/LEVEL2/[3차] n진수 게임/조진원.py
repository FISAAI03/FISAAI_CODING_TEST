# 10이상 숫자
num = dict({10 : 'A',
            11 : 'B',
            12 : 'C',
           13 : 'D',
           14 : 'E',
           15 : 'F'})

# 진법 변환 함수
def change(n, base) :
    answer = ''
    while n > 0 :
        k = n % base
        n = n // base
        if k < 10 :
            answer = str(k) + answer
        else :
            answer = num[k] + answer
    return answer


def solution(n, t, m, p):
    answer = ''
    
    # 전체 문자열
    game = '0'
    
    # 변환해서 넣기
    num = -1
    while len(game) < t*m :
        num += 1
        game += change(num, n)
    
    # 추출하기
    p -= 1
    while len(answer) < t :
        answer += game[p]
        p += m
    
    return answer
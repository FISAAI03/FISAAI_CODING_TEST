# 풀이시간: 17:17 ~ 18:04

'''
1. 1, 2, 4로 모든 수를 표현해야함
2. 1=1, 2=2, 4=3 취급
3. 3의 배수 단위까지 자릿수가 유지됨
4. 각 자리는 3까지 표현 가능
'''

def solution(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n, 3)
        if mod == 0:
            answer += '4'
            n -= 1
        else:
            answer += str(mod)

    answer = answer[::-1]

    return answer

solution(4)
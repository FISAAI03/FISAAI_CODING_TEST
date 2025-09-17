def solution(n):
    # 3진법의 원리로 푼다.
    # 단, 자릿수가 올라갈 때, 예외로 둔다.
    # 즉, 나눴을때 나머지가 0 이면 몫에서 하나 뺴고 그 자리를 4로 채운다.
    
    # answer 문자열 생성
    answer = ''
    while n > 0 :
        if n % 3 == 0 :
            answer = '4' + answer
            n = n//3 - 1
        else :
            answer = str(n%3) + answer
            n = n//3
    return answer

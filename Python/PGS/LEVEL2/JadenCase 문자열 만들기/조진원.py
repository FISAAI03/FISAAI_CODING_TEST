# 바로 앞 문자가 공백인지 아닌지 판별하기 위하여 'pre'라는 변수를 활용한다.


def solution(s):
    answer = ''
    pre = ' '
    for char in s :
        # 직전 값이 공백이라면
        if pre == ' ' :
            try :
                # 근데 숫자라면 그냥 추가
                int(char)
                answer += char
            except :
                # 그렇지 않으면 대문자로 바꾸기
                answer += char.upper()
        else :
            # 그 외에는 소문자로 추가
            answer += char.lower()
        
        # pre변수 업데이트
        pre = char
    return answer
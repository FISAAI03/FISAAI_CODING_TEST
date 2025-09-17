def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        answer += my_string[len(my_string)-1 -i]
    return answer

## len(my_string)은 정수임으로,  range(len(my_string)) 형태로 작성해야함

# sol 2
def solution(my_string):
    return my_string[::-1]

"""
# my_string[::-1]의 동작 원리
- [::-1]은 파이썬 슬라이싱 문법의 특별한 사용법입니다.

# 슬라이싱의 기본 문법은 다음과 같습니다:
# 파이썬 기본 문법: *** string[start:end:step] ***
- start: 슬라이싱을 시작할 인덱스 (기본값은 0).
- end: 슬라이싱을 종료할 인덱스 (기본값은 문자열 끝).
- step: 슬라이싱 진행 방향과 간격 (기본값은 1).

> 여기서 [::-1]의 의미:
- start, end는 생략: >> 전체 문자열을 선택.
- step = -1: >> 문자열을 역순으로 이동.

> 결과적으로, [::-1]은 문자열을 뒤집는 효과를 냅니다.
"""
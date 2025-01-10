# 풀이시간: 15:30 ~

'''
1. 숫자 비교를 통해 정렬을 해야함
2. 숫자 비교를 할 때 앞자리부터 비교
3. 주어진 숫자는 최대 4자리
4. 작은 자릿수 숫자 기준, 크기가 똑같을 때, 작은 자릿수 숫자가 먼저 배치되어야함
[발견]
5. 숫자 문자열 비교는 같은 자릿수 끼리는 숫자와 같음
6. 자릿수가 다를 경우 작은 자릿수가 크다 (틀림)
7. 3, 34 반례
[공부]
8. 파이썬 문자열 비교는 앞자리부터 순차적으로 비교
9. 3333, 30303030 일 경우 3 다음에 나오는 0으로 인해 3333이 더 크다
'''

def solution(numbers):
    answer = ''
    numbers_str = [str(num) for num in numbers]
    numbers_str = sorted(numbers_str, key = lambda x:x*4, reverse=True)
    answer = str(int(''.join(numbers_str)))
    return answer
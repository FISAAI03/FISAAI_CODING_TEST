from itertools import permutations
from collections import deque

# 두 숫자와 연산자를 받아 계산하는 함수
def calculate(num1, num2, operator):
    num1, num2 = int(num1), int(num2)
    if operator == '+': 
        return num1 + num2
    if operator == '-': 
        return num1 - num2
    if operator == '*': 
        return num1 * num2

def solution(expression):
    operators = ['+', '-', '*']  # 사용할 수 있는 연산자 목록
    
    # 수식을 숫자와 연산자로 분리하기
    tokens = deque()
    number = ''
    for ch in expression:
        if ch.isdigit():
            number += ch
        else:
            tokens.append(number)  # 숫자 추가
            tokens.append(ch)      # 연산자 추가
            number = ''
    tokens.append(number)          # 마지막 숫자 추가

    max_result = 0  # 가능한 가장 큰 절댓값 결과 저장
    
    # 연산자 우선순위의 모든 경우의 수(순열) 확인
    for priority in permutations(operators, 3):
        exp_copy = deque(tokens)  # 원본 토큰 복사
        
        # 현재 우선순위에 따라 연산자 순서대로 계산 수행
        for op in priority:
            new_tokens = deque()
            while exp_copy:
                token = exp_copy.popleft()
                if token == op:  
                    # 이전 숫자(new_tokens의 마지막 값)와 다음 숫자(exp_copy의 첫 값)를 꺼내서 계산
                    left = new_tokens.pop()
                    right = exp_copy.popleft()
                    new_tokens.append(calculate(left, right, op))
                else:
                    new_tokens.append(token)
            exp_copy = new_tokens
        
        # 결과값 절댓값 갱신
        max_result = max(max_result, abs(int(exp_copy[0])))
    
    return max_result

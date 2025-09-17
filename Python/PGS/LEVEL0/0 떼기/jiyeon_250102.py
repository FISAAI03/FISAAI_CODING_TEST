# SOL1
def solution(n_str):
    answer = ''  # 결과 저장 변수 초기화
    i = 0
    
    # 문자열을 처음부터 순회하면서 '0'이 아닌 첫 번째 문자를 찾음
    while i < len(n_str):
        if n_str[i] != '0':  # '0'이 아닌 문자를 만나면 반복문 종료
            break
        i += 1  # '0'이면 다음 문자로 이동
    
    # '0'이 제거된 부분부터 answer에 저장
    answer = n_str[i:]
    return answer


# SOL2
def solution(n_str):
    return n_str.lstrip('0')
    
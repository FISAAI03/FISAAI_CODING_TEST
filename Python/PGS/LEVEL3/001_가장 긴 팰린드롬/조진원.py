# 팰린드롬 판별함수
def is_pal(x) :
    return x == x[::-1]
        

def solution(s):
    # 초기 값은 전체 길이
    n = len(s)
    
    # 정답의 초기값은 0
    answer = 0
    
    # 부분 문자열 길이가 1이 될때까지 아래의 반복
    while n > 1 :
        # 인덱스 위치
        idx = 0
        while (idx + n) <= len(s) :
            # 팰린드롬이면 바로 반환
            if is_pal(s[idx:(idx+n)]) :
                return n
            idx += 1
        # 반영 안되었으면 길이 줄이기
        n -= 1
        
    return 1
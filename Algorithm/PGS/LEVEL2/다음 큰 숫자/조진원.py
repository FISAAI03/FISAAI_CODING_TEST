def solution(n):
    # 2진 변환 후에 1의 갯수 세기
    one_count = bin(n)[2:].count('1')
    
    # 탐색 가즈아
    while True :
        # 하나씩 키우기
        n += 1
        # 2진변환 후 1의 갯수가 같으면 멈추기
        if bin(n)[2:].count('1') == one_count :
            break
    return n
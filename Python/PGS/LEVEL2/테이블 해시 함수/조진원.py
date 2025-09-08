def solution(data, col, row_begin, row_end):
    # 1. col번째 컬럼 기준으로 오름차순, 값이 같으면 기본키(첫 번째 컬럼) 기준 내림차순 정렬
    sorted_data = sorted(data, key=lambda row: (row[col-1], -row[0]))
    
    # 2. 각 행에 대해 S_i 계산 후 리스트에 저장
    s_values = []
    for i in range(row_begin, row_end + 1):  # row_begin~row_end
        row = sorted_data[i - 1]
        s_sum = 0
        for value in row:
            s_sum += value % i  # 각 컬럼 값을 i로 나눈 나머지를 합산
        s_values.append(s_sum)
    
    # 3. S_i 값을 모두 XOR 연산하여 해시 값 계산
    hash_value = s_values.pop()  # 마지막 값으로 초기화
    while s_values:
        hash_value ^= s_values.pop()  # XOR 연산
    
    return hash_value

def solution(n):
    answer = 0
    
    # 투 포인터
    
    # start지점을 1부터
    for start in range(1, n+1) :
        # 합 값 초기화
        total = 0
        # end를 활용하여 연속된 값을 하나하나 더해준다.
        for end in range(start, n+1) :
            total += end
            # n값과 동일하면 값을 추가하고 중지
            if total == n :
                answer +=1
                break
            # 만약 n보다 커져도 중지
            elif total > n :
                break
    return answer
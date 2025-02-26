def solution(s):
    # 0 지운 횟수
    count1 = 0
    # 이진 변화 횟수
    count2 = 0
    
    # 무한반복
    while True :
        k = ''
        # 이진변화 시작
        count2 +=1
        
        # 0 걸러내기
        for n in s :
            if n == '1' :
                k += n
            else :
                count1 += 1
        # 걸러낸 결과 1 하나만 남으면 멈추기
        if k == '1' :
            break
        
        # 이진수 변환
        s = bin(len(k))[2:]
        
        # 결과가 1 하나만 남으면 걸러내기
        if s == '1' :
            break
    
    
    return [count2, count1]
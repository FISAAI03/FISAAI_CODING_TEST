def solution(n):
    
    # 기본 값 설정
    Fibo = [0, 1]
    
    # 0이면 0 배출
    if n == 0 :
        return 0
    
    # 1이면 1 배출
    elif n == 1 :
        return 1
    
    # 그렇지 않으면 n까지 수열만들기
    for _ in range(n-1) :
        Fibo.append(Fibo[-1] + Fibo[-2])
    
    # 마지막부분만 호출
    return Fibo[-1] % 1234567
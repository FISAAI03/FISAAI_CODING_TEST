def solution(numbers):
    # 문자열 변환
    numbers = list(map(str, numbers))
    
    # numbers의 길이는 최대 4자리
    # 그래서 한자리수가 4자리까지 늘어날 수 있도록 곱하기를 해서 비교
    # 예를들면, 3이랑 30이랑 두개를 비교했을 때, 4를 곱하면 3333 이랑 30303030이 나옴
    # 문자열 내림차순으로 비교하면 3333이 더 큰것으로 나오기 때문에 3이 앞으로 나온다.
    sort_number = sorted(numbers, key = lambda x : x*4, reverse=True)
    
    # 만약 모두가 0이면 0 하나만 나오게 해야 하기 대문에 일단 0으로 호출하기 위해 정수로 바꾼다음 다시 문자열로 바꿈
    answer = int(''.join(sort_number))
    return str(answer)
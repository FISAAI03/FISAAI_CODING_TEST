def solution(number, k):
    # 최종적으로 만들 숫자를 저장할 스택
    stack = []
    
    # 주어진 숫자 문자열에서 한 자리씩 순회
    for num in number:
        # 스택이 비어있지 않고
        # 아직 제거할 숫자 개수(k)가 남아 있고
        # 스택의 마지막 숫자가 현재 숫자보다 작다면
        # -> 큰 숫자를 앞으로 보내기 위해 작은 숫자를 제거
        while stack and k > 0 and stack[-1] < num:
            stack.pop()  # 스택의 마지막 숫자 제거
            k -= 1       # 제거할 숫자 개수 1 감소
        
        # 현재 숫자를 스택에 추가
        stack.append(num)
    
    # 반복문이 끝났는데도 제거할 숫자가 남아 있는 경우
    # (예: 숫자가 내림차순으로 정렬된 경우 pop할 조건을 못 만나므로)
    # 남은 k만큼 스택의 끝에서 제거
    if k > 0:
        stack = stack[:-k]
    
    # 스택에 남은 숫자들을 이어 붙여 문자열로 반환
    return ''.join(stack)

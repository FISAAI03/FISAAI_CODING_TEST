def solution(elements):
    # 함수 'solution'을 정의합니다. 입력으로 리스트 'elements'를 받습니다.
    answer = []
    # 결과를 저장할 빈 리스트 'answer'를 생성합니다.
    n = len(elements)
    # 'elements'의 길이를 'n'에 저장합니다.
    
    elements = elements * 2
    # 'elements' 리스트를 2배로 확장합니다. (연결된 리스트처럼 만들기 위함)
    for i in range(1, n+1):
        # 부분 리스트의 길이 'i'를 1부터 'n'까지 순회합니다.
        for j in range(n):
            # 시작 인덱스 'j'를 0부터 'n-1'까지 순회합니다.
            num = sum(elements[j:j+i])
            # 'elements' 리스트에서 'j'부터 'j+i'까지의 부분 리스트의 합을 'num'에 저장합니다.
            answer.append(num)
            # 부분 리스트의 합 'num'을 'answer' 리스트에 추가합니다.
    return len(set(answer))
    # 'answer' 리스트의 중복을 제거하고, 서로 다른 값의 개수를 반환합니다.

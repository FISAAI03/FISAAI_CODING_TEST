from collections import deque

def solution(weights):
    answer = 0

    # 몸무게별 사람 수를 저장하는 딕셔너리 생성
    weight_count = dict()
    for weight in weights:
        if weight not in weight_count:
            weight_count[weight] = 1
        else:
            weight_count[weight] += 1

    # 같은 몸무게끼리 짝꿍이 되는 경우: nC2 = n*(n-1)//2
    for weight in weight_count:
        count = weight_count[weight]
        if count > 1:
            answer += count * (count - 1) // 2

    # 몸무게 오름차순 정렬 후 deque로 변환
    sorted_weights = deque(sorted(list(weight_count)))

    current_weight = sorted_weights.popleft()

    # deque를 순회하며 비율 조건을 만족하는 다른 몸무게를 탐색
    while sorted_weights:
        for other_weight in sorted_weights:
            # 아래 조건은 각각 다음의 시소 거리 비율을 의미:
            # current_weight:other_weight = 2:3, 2:4, 3:4
            if current_weight * 3 == other_weight * 2 \
            or current_weight * 4 == other_weight * 2 \
            or current_weight * 4 == other_weight * 3:
                # 조건을 만족하면 가능한 쌍의 수를 더함
                answer += weight_count[current_weight] * weight_count[other_weight]

        # 다음 기준 몸무게로 이동
        current_weight = sorted_weights.popleft()

    return answer

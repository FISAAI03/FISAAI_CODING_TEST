def solution(k, tangerine):
    answer = 0
    tangerine_count = dict()
    for tangerine in tangerine:
        if tangerine in tangerine_count:
            tangerine_count[tangerine] += 1
        else:
            tangerine_count[tangerine] = 1

    # 귤의 빈도를 기준으로 내림차순 정렬
    sorted_tangerine = sorted(tangerine_count.items(), key=lambda x: x[1], reverse=True)

    total_tangerines = 0

    # 필요한 귤의 수가 만족될 때까지 종류를 추가
    for size, count in sorted_tangerine:
        total_tangerines += count
        answer += 1
        if total_tangerines >= k:
            break

    return answer

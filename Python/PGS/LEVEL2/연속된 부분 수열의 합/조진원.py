def solution(sequence, k):
    answer = []  
    start = 0    # 시작
    end = 0      # 끝
    total = sequence[0]  # 현재 윈도우 구간의 합
    min_length = len(sequence) + 1  # 현재까지 찾은 가장 짧은 구간의 길이

    # 투 포인터
    while start <= end and end < len(sequence):
        if total == k:
            # 구간 합이 k와 같은 경우
            if end - start + 1 < min_length:
                # 지금 구간이 이전에 찾은 구간보다 짧다면 정답 갱신
                min_length = end - start + 1
                answer = [start, end]
            # 다음 구간을 확인하기 위해 start를 한 칸 앞으로 이동하며 total도 감소
            total -= sequence[start]
            start += 1

        elif total < k:
            # 구간 합이 k보다 작으면 end를 오른쪽으로 확장하고 total 갱신
            end += 1
            if end < len(sequence):
                total += sequence[end]

        else:
            # 구간 합이 k보다 크면 start를 오른쪽으로 이동시켜 구간을 줄이고 total 갱신
            total -= sequence[start]
            start += 1

    return answer

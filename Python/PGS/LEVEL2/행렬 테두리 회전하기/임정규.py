def solution(rows, columns, queries):
    answer = []
    # 세팅
    arr = []
    count = 0
    for _ in range(rows):
        tmp = []
        for _ in range(columns):
            count += 1
            tmp.append(count)
        arr.append(tmp)

    # 풀이
    for query in queries:
        y1, x1, y2, x2 = query
        y1 -= 1
        x1 -= 1
        y2 -= 1
        x2 -= 1
        min_value = arr[y1][x1]
        # 구간은 4개
        # y1x1 ~ y1x2 상단
        # y1x2 ~ y2x2 우측
        # y2x2 ~ y2x1 하단
        # y2x1 ~ y1x1 좌측

        # 상단
        fix_num = arr[y1][x2]
        for idx in range(x2, x1, -1):
            min_value = min(min_value, arr[y1][idx])
            arr[y1][idx] = arr[y1][idx - 1]

        # 좌측
        for idx in range(y1, y2):
            min_value = min(min_value, arr[idx][x1])
            arr[idx][x1] = arr[idx + 1][x1]

        # 하단
        for idx in range(x1, x2):
            min_value = min(min_value, arr[y2][idx])
            arr[y2][idx] = arr[y2][idx + 1]

        # 우측
        for idx in range(y2, y1, -1):
            min_value = min(min_value, arr[idx][x2])
            arr[idx][x2] = arr[idx - 1][x2]

        # 보정
        arr[y1 + 1][x2] = fix_num

        answer.append(min_value)
    return answer
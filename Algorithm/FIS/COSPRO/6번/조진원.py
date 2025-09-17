def solution(start, locations) :
    answer = 0

    right = max(locations)
    left = min(locations)

    # 왼쪽갔다가 오른쪽가기
    case1 = abs(start-left) + (right-left)

    # 오른쪽갔다 왼쪽가기
    case2 = abs(start-right) + (right-left)

    return min(case1, case2)

start = 15
locations = [10, 62, 22]

print(solution(start, locations))
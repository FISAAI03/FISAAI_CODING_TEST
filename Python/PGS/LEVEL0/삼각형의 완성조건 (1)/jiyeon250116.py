def solution(sides):
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        return 1
    elif sides[2] >= sides[0] + sides[1]:
        return 2


# SOL2
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2
## 정렬이 필요 없음. 따라서 계산 비용이 낮음.
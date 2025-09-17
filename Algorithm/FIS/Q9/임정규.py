import sys
sys.setrecursionlimit(100_000)

def find(a, p):
    if a == p[a]:
        return a
    p[a] = find(p[a], p)
    return p[a]

def union(a, b, p):
    pa = find(a, p)
    pb = find(b, p)
    p[pa] = pb # 순서는 상관없음

def solution(N, info, game):
    result = 0

    # 세팅
    p = [0] * N
    for idx in range(N):
        p[idx] = idx

    # 집합 만들기
    for i in range(len(game)):
        start = game[i][0]
        for j in range(len(game[i])):
            union(start, game[i][j], p)

    # 찾기
    for i in range(len(game)):
        flag = True
        game_idx = game[i][0]
        for j in range(info[0][0]):
            if find(game_idx, p) == find(info[1][j], p):
                flag = False
                break
        if flag == True:
            result += 1

    return result


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
N = 5
info = [[ 1 ], [ 4 ]]
game = [[1, 2], [3], [3, 4]]
ret = solution(N, info, game)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

N = 7
info = [[ 3 ], [ 1, 2, 3 ]]
game = [[1], [2], [3], [4], [5], [6], [4, 5], [3, 6]]
ret = solution(N, info, game)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
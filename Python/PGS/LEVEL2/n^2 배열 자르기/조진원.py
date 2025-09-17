# 일단 문제에 나온대로 하면 시간초과가 뜸
# 1. 행렬 -> 리스트가 아닌 리스트 -> 행렬로 생각하면 행은 몫, 열은 나머지가 된다.
# 2. 특정 범위 값들만 뽑아서 안의 값을 구한다.
# 3. 안에 들어가는 값은 행과 열 중 큰 값 +1 로 채워지는 규칙을 가지고 있다.


def solution(n, left, right):
    answer = []
    
    for number in range(left, right+1) :
        row = number // n
        col = number % n
        
        k = max(row,col) + 1
        answer.append(k)

    return answer
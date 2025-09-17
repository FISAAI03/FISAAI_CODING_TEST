def solution(slice, n):
    if slice > n:
        return 1
    elif slice <= n:
        if n%slice == 0:
            return n//slice
        else:
            return n//slice +1

# sol 2
def solution(slice, n):
    return ((n - 1) // slice) + 1

## n-1을 하면 올림하는 효과가 나기 때문에, 몫으로 간단하게 계산할 수 있게됨
"""
print(solution(7, 10))  # 출력: 2
print(solution(4, 12))  # 출력: 3
print(solution(4, 13))  # 출력: 4
print(solution(8, 16))  # 출력: 2
"""

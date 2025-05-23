import sys

input = sys.stdin.readline

n, m = map(int, input().split())

visited = []

# 재귀를 활용한 백트래킹으로 start변수를 통한 조합 출력 함수
def backtrack(start):
    if len(visited) == m:
        print(*visited)
        return

    for i in range(start, n+1):
        if i not in visited:
            visited.append(i)
            backtrack(i+1)
            visited.remove(i)

backtrack(1)
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

visited = []

# 재귀를 활용한 백트래킹 활용
def backtrack(start):
    if len(visited) == m:
        print(*visited)
        return

    for i in range(start, n+1):
        visited.append(i)
        backtrack(i)
        visited.pop()

backtrack(1)
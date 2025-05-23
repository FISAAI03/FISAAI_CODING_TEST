import sys

input = sys.stdin.readline

n, m = map(int, input().split())
seq = sorted(list(map(int, input().split())))

visited = []

# 재귀를 활용한 백트래킹 활용
def backtrack(start):
    if len(visited) == m:
        print(*visited)
        return

    for i in range(start, len(seq)):
        visited.append(seq[i])
        backtrack(i+1)
        visited.pop()

backtrack(0)
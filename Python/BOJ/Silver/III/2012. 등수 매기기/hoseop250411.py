import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

queue = []
for _ in range(n):
    queue.append(int(input()))

queue = deque(sorted(queue))
index = 1
summ = 0

# 예상 등수가 높은 순위부터 차례로 불만도 합 계산
while queue:
    summ += abs(queue.popleft() - index)
    index += 1

print(summ)
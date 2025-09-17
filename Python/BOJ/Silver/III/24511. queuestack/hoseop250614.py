import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(input().split())
m = int(input())
C = list(input().split())

# 스택인 것들(1)은 먼저 들어온 값이 먼저 나가므로 원소값 고정
# 큐인 것들(0)만 모아서 다시 리스트 재생성
A0 = deque([])
for i in range(n):
    if A[i] == 0:
        A0.append(B[i])

# 리스트 거꾸로 정렬
A0.reverse()

# 오른쪽으로 삽입하고 왼쪽으로 팝
for j in C:
    A0.append(j)
    print(A0.popleft(), end=' ')
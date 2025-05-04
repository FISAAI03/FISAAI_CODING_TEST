import sys

input = sys.stdin.readline
n = int(input())

a = [int(input()) for _ in range(n)][::-1]

seq = []
# 그리디 삽입 - a값(ai)을 거꾸로 돌면서 n에서 1까지 순차적으로 ai인덱스 값에 i삽입
for ai, i in zip(a, range(n, 0, -1)): # 시간 복잡도 O(n)
    seq.insert(ai, i) # 시간 복잡도 O(n)

for i in seq:
    print(i)
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

s = set()
for _ in range(n):
    s.add(input().strip())

cnt = 0
for _ in range(m):
    st = input().strip()
    if st in s:
        cnt += 1

print(cnt)
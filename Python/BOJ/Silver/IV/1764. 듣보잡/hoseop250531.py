import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst = set()
for _ in range(n):
    lst.add(input().strip())

ans = []
for _ in range(m):
    name = input().strip()
    if name in lst:
        ans.append(name)

ans.sort()
print(len(ans))
for i in ans:
    print(i)
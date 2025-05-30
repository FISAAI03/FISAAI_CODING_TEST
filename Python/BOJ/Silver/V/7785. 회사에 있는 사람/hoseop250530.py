import sys

input = sys.stdin.readline

n = int(input())

sets = set()

for _ in range(n):
    name, state = input().split()
    if state == 'enter':
        sets.add(name)
    else:
        sets.remove(name)

for i in sorted(list(sets), reverse=True):
    print(i)
import sys

input = sys.stdin.readline

n = int(input())

coor = list(map(int, input().split()))

reduc = {}
for i, j in enumerate(sorted(list(set(coor)))):
    reduc[j] = i

for x in coor:
    print(reduc[x], end=' ')
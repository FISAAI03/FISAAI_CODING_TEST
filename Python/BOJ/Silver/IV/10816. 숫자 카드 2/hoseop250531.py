import sys

input = sys.stdin.readline

n = int(input())
nlst = list(map(int, input().split()))
m = int(input())
mlst = list(map(int, input().split()))

nlst.sort()

hash = {}
i = 0
while i < n:
    if nlst[i] not in hash:
        hash[nlst[i]] = 1
    else:
        hash[nlst[i]] += 1
    i += 1

for i in mlst:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')

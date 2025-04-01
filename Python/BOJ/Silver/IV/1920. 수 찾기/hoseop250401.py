import sys

input = sys.stdin.readline

hash_map = {}
n = int(input())
A = list(map(int, input().split()))

# 해쉬맵에 key=A값, value=1 로 저장
for i in A:
    hash_map[i] = 1

m = int(input())

for j in list(map(int, input().split())):
    # 해쉬맵에서는 검색의 시간복잡도가 O(1)이므로 최적화 가능
    if j in hash_map:
        print(1)
    else:
        print(0)
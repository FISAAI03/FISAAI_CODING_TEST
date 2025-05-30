import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 빠른 탐색을 위해 해쉬 맵을 이름용, 숫자용으로 두 개를 만들어줌
name_dogam = {}
num_dogam = {}
for num in range(1, n+1):
    pocketmon = input().strip()
    name_dogam[pocketmon] = num
    num_dogam[num] = pocketmon

for _ in range(m):
    q = input().strip()
    if q.isalpha():
        print(name_dogam[q])
    else:
        print(num_dogam[int(q)])

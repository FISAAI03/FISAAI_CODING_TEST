n = int(input())
n_card = list(map(int, input().split()))
m = int(input())
m_card = list(map(int, input().split()))

hash_map = {}

for nc in n_card:
    hash_map[nc] = 1

ans = []
for mc in m_card:
    if mc in hash_map:
        ans.append(1)
    else:
        ans.append(0)

for i in ans:
    print(i, end=' ')
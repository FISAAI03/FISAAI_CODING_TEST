from collections import defaultdict

n = int(input())

infor = defaultdict(list)

for _ in range(n):
    age, name = input().split()
    infor[int(age)].append(name)

for i in sorted(infor.keys()):
    for j in infor[i]:
        print(f'{i} {j}')

import sys
from collections import Counter

n = int(sys.stdin.readline())

if n == 1:
    num = int(sys.stdin.readline())
    for _ in range(3):
        print(num)
    print(0)

else:
    nlst = []

    for _ in range(n):
        nlst.append(int(sys.stdin.readline()))

    nlst.sort()

    # 평균값
    avg = round(sum(nlst)/n)
    # 중앙값
    mid = nlst[n//2]
    # 최빈값
    counter = Counter(nlst).most_common()
    mode = 0
    if len(counter) > 1 and (counter[0][1] == counter[1][1]):
        mode_lst = [ k for k, v in counter if counter[0][1] == v]
        mode = sorted(mode_lst)[1]
    else:
        mode = counter[0][0]
    # 범위
    rangee = nlst[-1] - nlst[0]

    print(avg)
    print(mid)
    print(mode)
    print(rangee)
## Sort/Loop 조합을 활용하여 문제 해결

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p_num = []
    for _ in range(n):
        p_num.append(input().strip())

    # 숫자 문자열 리스트를 사전순으로 정렬
    # 사전순으로 정렬하면 접두어가 같은 것들 순으로 인접하게 정렬해줌
    p_num.sort()

    flag = True
    
    # 정렬을 활용하여 2중 loop를 1중 loop로 줄여 앞 뒤 값들만 비교하여 일관성 확인
    for p1, p2 in zip(p_num, p_num[1:]):
        if p2.startswith(p1):
            flag =  False
            break

    if flag:
        print('YES')
    else:
        print('NO')
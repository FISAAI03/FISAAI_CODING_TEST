import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    # n값에 따라 할당 경우의 수를 나누어 줌줌
    if n == 0:
        input()
        lst = deque([])
    elif n == 1:
        lst = deque([input()[1:-2]])
    else:
        lst = deque(list(map(int, input()[1:-2].split(','))))

    # front는 R을 만날 때마다 값을 갱신해주어 앞에서 값을 뺄지 뒤에서 뺄지 이정표 역할
    # flag는 lst 안에 값이 있으면 True, 없으면 False로 error 여부 확인 역할
    front = True
    flag = True
    for i in p:
        if i == 'R':
            front = False if front else True
        else:
            if lst:
                if front:
                    lst.popleft()
                else:
                    lst.pop()
            else:
                # 값이 없는데 D를 만났을 경우 error 출력하기 위함
                flag = False
                break
    if flag:
        if not front:
            lst.reverse()
        print(f"[{','.join(map(str, lst))}]")
    else:
        print('error')
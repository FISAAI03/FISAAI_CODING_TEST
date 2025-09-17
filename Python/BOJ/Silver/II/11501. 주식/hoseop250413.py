import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):    

    N = int(input())
    stock = list(map(int, input().split()))
    max_stock = stock[-1]
    max_profit = 0

    # 뒤에서 앞으로 가면서 시간에 따른 max_stock을 유지하며 최대 이익을 최적화하여 계산
    for i in range(N-2, -1, -1):
        if max_stock < stock[i]:
            max_stock = stock[i]
        else:
            max_profit += max_stock - stock[i]

    print(max_profit)

import sys

input = sys.stdin.readline

T = int(input())
''' 
* 둘 다 최선의 플레이를 할 경우, 겹치지 않은 2개의 비안전지대를 제외한 모든 지역에 경비를 배치함.

nxm 격자판에서 겹치지 않은 2개의 kxk 정사각형(배반사건)을 제외한 지역 크기가
짝수일 경우, 배반사건인 비안전지대(kxk 정사각형) 하나를 유토가 안전지대로 만들면, 플라티나가 마지막으로 안전지대를 점유
홀수일 경우, 배반사건인 비안전지대(kxk 정사각형) 하나를 플라티나가 안전지대로 만들면, 유토가 마지막으로 안전지대를 점유
'''
for _ in range(T):
    n, m, k = map(int, input().split())
    # n, m의 범위가 2*k보다 작을 경우, 무조건 첫 턴의 사람이 승리
    if (n < 2*k) and (m < 2*k):
        print('Yuto')
    elif (n*m - 2*k*k) % 2 == 0:
        print('Platina')
    else:
        print('Yuto')
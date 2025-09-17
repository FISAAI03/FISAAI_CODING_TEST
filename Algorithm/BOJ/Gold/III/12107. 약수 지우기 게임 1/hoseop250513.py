import sys

input = sys.stdin.readline

n = int(input())

# 2~n 까지의 수 중 하나를 첫 번째 경우의 수로 선택하여 
# 이기는 사람은 1을 먼저 선택하여 결과를 바꿀 수 있으므로 1보다 크면 무조건 A가 승리
if n > 1:
    print('A')
else:
    print('B')
# DP 규칙 -> SK, CY, SK, SK, SK, SK, CY / 7개 경우의 수로 반복

n = int(input())

r = n % 7

if r == 2 or r == 0:
    print('CY')
else:
    print('SK')
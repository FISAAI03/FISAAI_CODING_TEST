# DP 규칙 -> SK, CY, SK, SK, CY / 5개 경우의 수로 반복
n = int(input())

r = n % 5

if r == 2 or r == 0:
    print('CY')
else:
    print('SK')
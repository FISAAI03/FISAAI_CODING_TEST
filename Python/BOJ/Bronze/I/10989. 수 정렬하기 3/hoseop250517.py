import sys

input = sys.stdin.readline

n = int(input())

# 1~10000까지의 수들의 출현 횟수 저장
cnt = [0] * 10001

# 입력값을 받아 숫자들의 count 횟수 업데이트
for _ in range(n):
    num = int(input())
    cnt[num] += 1

# 인덱스 번호(숫자)에 맞게 count 횟수 만큼 차례로 반복해서 출력
for i in range(1, len(cnt)):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)
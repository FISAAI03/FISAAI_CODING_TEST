a, b = map(int, input().split())

cnt = 1
# b를 줄여서 a값 보다 작아질 때까지 반복복
while b > a:
    # b의 1의 자리가 1이 아니고 홀수 일 때, 무조건 -1이므로 반복문 빠져나감
    if (b%10 != 1) and (b%2 == 1):
        break
    # b가 짝수 일때는 2로 나눔
    elif (b%2 == 0):
        b = b//2
        cnt += 1
    # b의 1의 자리가 1인 경우 10으로 나눈 몫으로 갱신
    else:
        b = b//10
        cnt += 1

if b != a:
    print(-1)
else:
    print(cnt)

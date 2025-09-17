# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(numberA, numberB, limit):
    # 여기에 코드를 작성해주세요.
    answer = [0] * 1001
    answer[0] = 1

    start = min(numberA, numberB)
    for making_sum in range(start, limit + 1):
        if making_sum - numberA >= 0 and answer[making_sum - numberA] == 1:
            answer[making_sum] = 1
        if making_sum - numberB >= 0 and answer[making_sum - numberB] == 1:
            answer[making_sum] = 1

    return sum(answer[1:])
# DP 중복값 회피
# 아이디어 정리
# 만들어야하는 총합에서 주어진 숫자를 빼고, 남은 숫자가 만들 수 있는 숫자면 갱신
# 0은 만들 수 있는 숫자인데, 문제에서 제외.


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 
numberA1 = 2
numberB1 = 4
limit1 = 10
ret1 = solution(numberA1, numberB1, limit1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

numberA2 = 2
numberB2 = 3
limit2 = 10
ret2 = solution(numberA2, numberB2, limit2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
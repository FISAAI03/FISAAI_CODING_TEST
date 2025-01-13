# 최소공배수 구하는 함수
def lcm(a,b) :
    # 정렬하기
    num1, num2 = max(a,b), min(a,b)
    
    # 유클리드호제법
    while True :
        # 나누었을 때 나머지가 0이면 그것이 최대공약수
        if num1%num2 == 0 :
            gcd = num2
            break
        else :
        # 몫과 나머지로 계속 업데이트 한다.
            num1, num2 = num2, num1%num2
    
    # 최소공배수 구하는 계산
    return gcd * (a//gcd) * (b//gcd)


def solution(arr):
    # 값에서 하나 뺀다.
    answer = arr.pop()
    # arr을 비울때까지 반복
    while len(arr) > 0 :
        # 하나를 빼서
        num = arr.pop()
        # 최소공배수를 계산
        answer = lcm(answer,num)
    return answer
# 풀이시간 : 14:12 ~ 15:14

'''
1. x보다 큰 수 중 2자리 수 이하로 차이나는 제일 작은 수를 찾아야 한다.
2. 규칙성을 찾아보자.
  01, 10, 011, 101, 110, 0111, 1011

3. 0이 등장하면 뒤에 1과 위치가 바뀐다
4. 예외, 첫째자리가 0이면 1을 더해 바꾸어 준다
5. 이외의 자리는 바로 뒤 자릿수 만큼 더해 바꾸어준다.
'''

def solution(numbers):
    answer = []

    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            idx = 0
            save = num
            while True:
                if num % 2 == 0:
                    answer.append(save + 2**(idx - 1))
                    break
                else:
                    num = num // 2
                    idx += 1
    return answer
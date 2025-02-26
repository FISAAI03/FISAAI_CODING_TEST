def solution(n):
    answer = 0

    tmp2 = 0
    for i in range(n):
        if i < 2:
            tmp = i
            answer += i
        else:
            tmp2 = answer
            answer += tmp
            tmp = tmp2

    return answer % 1234567
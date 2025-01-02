# SOL1
def solution(num_list):
    answer = 0
    
    for num in num_list:
        while num > 1:
            if num % 2 == 0:  # 짝수인 경우
                num //=  2      # num = num // 2와 같은 코드
            else:  # 홀수인 경우
                num = (num-1)  // 2
            answer += 1
    return answer


# SOL2
def solution(num_list):
    answer = 0

    for n in num_list:
        while n != 1:
            n //= 2
            answer += 1

    return answer


# SOL3
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)

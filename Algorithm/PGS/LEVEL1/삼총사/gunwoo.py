from itertools import combinations as comb

def solution(number):
    answer = 0
    com = list(comb(number, 3))
    for i in range(len(com)):
        if sum(com[i]) == 0:
            answer +=1
            
    return answer

#combinations 알면 쉬운 문제
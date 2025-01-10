# 풀이시간: 12:02 ~ 1:24

'''
0. 보트에는 최대 2명이 탈 수 있다. (놓쳤음)
1. 몸무게를 내림차순으로 정렬 필요
2. 가장 무거운 사람, 가장 가벼운 사람 투포인터로 풀이
'''

def solution(people, limit):
    answer = 0

    sorted_people = sorted(people, reverse=True)
    start = 0
    end = len(sorted_people) - 1

    while start <= end:
        answer += 1
        check = sorted_people[start] + sorted_people[end]
        if check > limit:
            start += 1
        else:
            start += 1
            end -= 1

    return answer
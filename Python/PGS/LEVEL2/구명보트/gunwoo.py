def solution(people, limit):
    s = 0
    l = len(people)-1
    people = sorted(people)
    answer = 0
    while s <= l:
        if people[s] + people[l] <= limit:
            s += 1
        l -= 1
        answer += 1
        
    return answer
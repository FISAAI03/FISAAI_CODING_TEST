def solution(names):
    answer = []
    if len(names) < 5:
            answer.append(names[0])
    else:
        a = int(len(names)/5+1)
        for i in range(0, len(names), 5):
            answer.append(names[i])
    return answer
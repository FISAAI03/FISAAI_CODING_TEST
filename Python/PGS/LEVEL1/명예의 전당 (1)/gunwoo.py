def solution(k, score):
    answer = []
    for i in range(len(score)):
        while k > i:
            answer.append(min(score[0:i+1]))
            break
        if k <= i:
            scored = sorted(score[0:i+1], reverse = True)
            answer.append(scored[k-1])
    return answer
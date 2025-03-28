from collections import deque

def solution(progresses, speeds):
    answer = []

    q = deque(progresses)

    day = 1
    idx = 0
    count = 0
    while q:
        if (q[0] + (day * speeds[idx])) < 100:
            day += 1
            if count != 0:
                answer.append(count)
                count = 0
        else:
            q.popleft()
            idx += 1
            count += 1

    if count != 0:
        answer.append(count)

    return answer
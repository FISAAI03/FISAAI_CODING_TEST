from collections import deque

def solution(prices):
    answer = []

    q = deque(prices)

    while q:
        tmp = q.popleft()
        count = 0
        for i in q:
            count += 1
            if i < tmp:
                break
        answer.append(count)

    return answer
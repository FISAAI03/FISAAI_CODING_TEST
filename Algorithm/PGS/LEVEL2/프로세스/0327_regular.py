from collections import deque

def solution(priorities, location):
    answer = 0

    q = deque()
    stack = sorted(priorities)
    for idx, weight in enumerate(priorities):
        q.append((idx, weight))

    while q:
        current = q.popleft()
        if current[1] < stack[-1]:
            q.append(current)
        else:
            answer += 1
            stack.pop()
            if current[0] == location:
                break

    return answer
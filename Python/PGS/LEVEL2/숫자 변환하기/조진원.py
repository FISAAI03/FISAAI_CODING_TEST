# 재귀로 하려니 시간초과 무조건 뜸
# DP로 풀자!

from collections import deque

def solution(x, y, n):
    if x > y:
        return -1

    queue = deque([(x, 0)])  # (현재 값, 연산 횟수)
    visited = set([x])       # 방문한 숫자 저장
    
    while queue:
        current, count = queue.popleft()
        
        if current == y:
            return count
        
        # 가능한 연산 수행
        for next_value in [current * 2, current * 3, current + n]:
            if next_value <= y and next_value not in visited:
                visited.add(next_value)
                queue.append((next_value, count + 1))
    
    return -1
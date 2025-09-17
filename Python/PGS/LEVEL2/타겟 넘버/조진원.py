from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])  # 초기 상태: (인덱스, 합계)
    answer = 0
    
    while queue:
        i, total = queue.popleft()
        
        if i == len(numbers):  # 모든 숫자를 다 탐색한 경우
            if total == target:  # 목표 값과 일치하면
                answer += 1
        else:
            # 현재 숫자를 더하거나 빼는 두 가지 경우를 큐에 추가
            queue.append((i + 1, total + numbers[i]))
            queue.append((i + 1, total - numbers[i]))
    
    return answer
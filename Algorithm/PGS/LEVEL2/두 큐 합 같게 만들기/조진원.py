from collections import deque

def solution(queue1, queue2):
    # 리스트를 큐로 변환 (deque는 popleft와 append 연산이 빠름)
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 각 큐의 합 구하기
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    # 두 큐의 총합이 홀수이면 두 큐의 합을 같게 만드는 것은 불가능
    if (sum1 + sum2) % 2 != 0 :
        return -1
    
    # 두 큐가 같아지기 위해 목표로 해야 하는 합
    target = (sum1 + sum2) // 2
    
    # 이동 횟수 카운트
    count = 0
    # 큐의 길이 총합 * 2 이상이면 무한 루프 가능성이 있어 제한
    while count <= 2*(len(q1) + len(q2)) :
        # q1의 합이 목표값과 같아졌으면 종료
        if sum1 == target :
            return count
        # q1의 합이 더 크면 q1에서 원소를 꺼내 q2로 이동
        elif sum1 > target :
            t = q1.popleft()
            sum1 -= t
            
            q2.append(t)
            sum2 += t
        # q2의 합이 더 크면 q2에서 원소를 꺼내 q1으로 이동
        else :
            t = q2.popleft()
            sum2 -= t
            
            q1.append(t)
            sum1 += t
        
        # 이동 횟수 증가
        count += 1
    
    # 위 조건 내에서 두 큐의 합이 같아지지 않으면 -1 반환
    return -1

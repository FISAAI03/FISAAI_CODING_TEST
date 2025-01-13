from collections import deque

def solution(prices):
    answer = []
    
    # 큐로 변환
    prices = deque(prices)
    
    # 무한루프 시작
    while True :
        # 거리는 0
        term = 0
        # 맨 왼쪽 값을 뺀다.
        k = prices.popleft()
        
        # 만약 뺐는데 기존 리스트가 비어있으면 멈추고 0을 넣는다.
        if len(prices) == 0 :
            answer.append(term)
            break
        
        # 남아있는 price리스트를 탐색
        for price in prices :
            # term을 한단계씩 더하면서
            term += 1
            # 만약 떨어지는 구간이 발생하면 멈춤
            if price < k :
                break
        
        # 도출된 term 값들을 answer에 추가
        answer.append(term)
    return answer
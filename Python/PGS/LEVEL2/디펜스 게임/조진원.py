import heapq

def solution(n, k, enemy):
    heap = [] # 무적권 쓸 병력
    
    for i, e in enumerate(enemy):
        
        # 아직 무적권이 아직 채워지지 않으면 우선 채움
        if len(heap) < k:
            heapq.heappush(heap, e)  # 최소 힙에 적 공격 병력 수 추가
            continue  # 다음 공격으로 넘어감

        # 최소 힙에서 가장 작은 병력 수보다 이번 공격이 크면 교체
        if heap[0] < e:
            n -= heapq.heappop(heap)  # 최소 힙에서 작은 공격을 빼고 병력 사용
            heapq.heappush(heap, e)   # 이번 공격을 힙에 추가하여 k번 무적권 사용 기록
        else:
            n -= e  # 이번 공격을 병력으로 막음
        
        # 만약 0보다 작아지면 반환
        if n < 0:
            return i
    
    # 모두 통과했다면 반환
    return len(enemy)

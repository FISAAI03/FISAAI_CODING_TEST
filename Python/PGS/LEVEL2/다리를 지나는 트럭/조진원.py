from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0  # 총 소요 시간
    sum_weight = 0  # 현재 다리 위 트럭들의 총 무게
    truck_weights = deque(truck_weights)  # 대기 중인 트럭들을 큐로 변환
    
    # 다리를 나타내는 큐 생성 (초기에는 모두 0으로 채움)
    bridge = deque([0 for _ in range(bridge_length)])
    
    # 트럭이 다리를 모두 건널 때까지 반복
    while True:
        # 매 초마다 다리에서 트럭 한 칸 이동 (맨 앞 트럭은 다리에서 나감)
        b = bridge.popleft()
        sum_weight -= b  # 다리에서 나간 트럭의 무게만큼 총 무게 감소

        # 아직 대기 중인 트럭이 있다면
        if len(truck_weights) > 0:
            # 다리 위에 트럭을 더 올릴 수 있는지 확인
            if sum_weight + truck_weights[0] <= weight:
                # 가능하면 트럭을 다리에 올림
                truck = truck_weights.popleft()
                sum_weight += truck
                bridge.append(truck)
            else:
                # 무게 초과라면 트럭 없이 0만 추가 (다리 위 공간만 차지)
                bridge.append(0)
        else:
            # 대기 중인 트럭이 없다면 다리 위의 트럭만 이동
            bridge.append(0)
        
        answer += 1  # 시간 1초 증가

        # 더 이상 다리 위에도, 대기열에도 트럭이 없으면 종료
        if sum_weight == 0 and len(truck_weights) == 0:
            break

    return answer  # 모든 트럭이 다리를 건너는 데 걸린 총 시간

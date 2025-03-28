from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    q = deque([0 for _ in range(bridge_length)])
    arrived = []
    idx = 0

    while arrived != truck_weights:
        answer += 1
        tmp = q.popleft()
        if tmp != 0:
            arrived.append(tmp)
            weight += tmp
        if (idx < (len(truck_weights))) and (weight - truck_weights[idx] >= 0):
            q.append(truck_weights[idx])
            weight -= truck_weights[idx]
            idx += 1
        else:
            q.append(0)

    return answer

### sum() 시간복잡도를 생각보다 많이 잡아먹음.
### 최대 무게 비교가 아닌 가감하는 방식으로 풀면 시간 복잡도가 획기적으로 줄어듬
from collections import deque

# 전력망이 나뉘었을 때 각각의 연결된 송전탑 수를 구하는 함수
def count_connected_towers(n, wires):
    # 그래프 초기화 (1번부터 n번 송전탑까지)
    graph = {i: [] for i in range(1, n+1)}
    
    # 양방향 연결 정보 추가
    for tower1, tower2 in wires:
        graph[tower1].append(tower2)
        graph[tower2].append(tower1)

    visited = [False] * (n + 1)  # 방문 여부 확인 리스트
    component_sizes = []  # 연결된 송전탑 수 저장 리스트

    # 모든 송전탑을 순회하며 BFS 수행
    for start_node in range(1, n + 1):
        if not visited[start_node]:
            queue = deque([start_node])
            visited[start_node] = True
            connected_count = 1  # 현재 연결된 송전탑 수

            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                        connected_count += 1
            
            component_sizes.append(connected_count)

    return component_sizes

# 전선을 하나씩 끊어보며 두 전력망의 송전탑 개수 차이의 최솟값 구하기
def solution(n, wires):
    min_difference = n  # 초기값은 송전탑 최대 개수로 설정

    # 모든 전선을 하나씩 끊어보며 시뮬레이션
    for i in range(n-1):
        # i번째 전선을 제외한 나머지 전선으로 임시 전력망 구성
        temp_wires = wires[:i] + wires[i+1:]

        # 전선 끊은 후 연결된 송전탑 수 계산
        connected_sizes = count_connected_towers(n, temp_wires)

        # 두 개의 네트워크로 나뉘었는지 확인
        if len(connected_sizes) == 2:
            size1, size2 = connected_sizes
        else:
            size1 = connected_sizes[0]
            size2 = 0  # 하나로만 연결된 경우

        # 송전탑 수 차이의 절댓값 계산
        difference = abs(size1 - size2)
        min_difference = min(min_difference, difference)

    return min_difference

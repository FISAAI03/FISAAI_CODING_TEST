from collections import deque

def solution(N, road, K):
    
    # 1. 그래프 초기화
    # N+1개의 빈 리스트를 만들어 각 노드별로 연결된 노드와 거리를 저장
    graph = [[] for _ in range(N+1)]
    for s, e, d in road:
        # 양방향 도로이므로 서로 연결
        graph[s].append((e, d))  # s에서 e까지 거리 d
        graph[e].append((s, d))  # e에서 s까지 거리 d

    # 2. 각 노드까지의 최단 거리 배열 초기화
    dist = [float('inf')] * (N+1)  # 처음에는 모든 거리를 무한대로 설정
    dist[1] = 0  # 시작점(노드 1)까지의 거리는 0

    # 3. BFS 탐색을 위한 큐 초기화
    queue = deque([1])  # 시작점 노드 1을 큐에 넣음

    # 4. BFS 방식으로 최단 거리 갱신
    while queue:
        node = queue.popleft()  # 큐에서 노드 하나 꺼내기
        for nei, w in graph[node]:  # 해당 노드와 연결된 모든 노드 탐색
            # 현재 기록된 거리보다 더 짧은 경로가 발견되면 갱신
            if dist[nei] > dist[node] + w:
                dist[nei] = dist[node] + w  # 최단 거리 갱신
                queue.append(nei)  # 갱신된 노드를 큐에 추가하여 다시 탐색

    # 5. K 이하 거리의 마을 개수 세기
    answer = 0
    for i in dist:
        if i <= K:  # 최단 거리가 K 이하이면
            answer += 1  # 마을 개수 증가

    return answer
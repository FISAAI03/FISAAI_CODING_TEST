def solution(n, computers):
    # 네트워크의 개수를 세는 변수 초기화
    network_count = 0
    # 각 컴퓨터의 방문 여부를 기록하는 리스트 초기화 (n개의 컴퓨터가 있으므로 n개의 False로 시작)
    visited = [False for _ in range(n)]
    
    # 모든 컴퓨터를 순회
    for computer in range(n):
        # 만약 현재 컴퓨터를 이미 방문했다면 (즉, 이미 어떤 네트워크에 포함되어 있다면)
        if visited[computer]:
            # 다음 컴퓨터로 넘어감
            continue
        # 아직 방문하지 않은 컴퓨터라면
        else:
            # 새로운 네트워크를 발견했으므로 네트워크 개수를 1 증가
            network_count += 1
            # DFS(깊이 우선 탐색)를 위한 스택 초기화. 현재 컴퓨터부터 탐색 시작.
            stack = [computer]
            
            # 스택이 비어있지 않은 동안 (즉, 현재 네트워크에 연결된 모든 컴퓨터를 탐색할 때까지)
            while stack:
                # 스택의 가장 위에 있는 컴퓨터를 꺼냄
                current_computer = stack.pop()
                # 현재 컴퓨터를 방문 처리
                visited[current_computer] = True
                
                # 현재 컴퓨터와 연결된 다른 모든 컴퓨터를 순회
                for neighbor in range(n):
                    # 만약 현재 컴퓨터와 neighbor 컴퓨터가 연결되어 있고 (computers[current_computer][neighbor] == 1)
                    # 아직 neighbor 컴퓨터를 방문하지 않았다면
                    if computers[current_computer][neighbor] == 1 and not visited[neighbor]:
                        # neighbor 컴퓨터를 스택에 추가하여 나중에 탐색하도록 함
                        stack.append(neighbor)
                        # neighbor 컴퓨터를 방문 처리 (중복 방문 방지 및 효율적인 탐색을 위해 스택에 추가할 때 바로 방문 처리)
                        visited[neighbor] = True
                        
    # 모든 탐색이 끝난 후 발견된 네트워크의 총 개수를 반환
    return network_count
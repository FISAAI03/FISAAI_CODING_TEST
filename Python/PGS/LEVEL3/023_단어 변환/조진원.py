from collections import deque

def solution(begin, target, words):
    
    # (현재 단어, 변환 횟수)를 큐에 넣고 시작
    queue = deque([(begin, 0)])
    
    # target이 words 안에 없다면 변환 불가능 → 0 반환
    if target not in words:
        return 0
    
    # BFS 시작
    while queue:
        char, d = queue.popleft()  # 현재 단어(char), 변환 횟수(d)
        
        # 목표 단어에 도달하면 현재까지의 변환 횟수 반환
        if char == target:
            return d

        # words 리스트에 있는 모든 단어를 확인
        for word in words:
            chk = 0  # 서로 다른 알파벳 개수 카운트
            for w1, w2 in zip(list(char), list(word)):
                if w1 != w2:
                    chk += 1
            
            # 한 글자만 다르면 변환 가능 → 큐에 추가
            if chk == 1:
                queue.append((word, d+1))

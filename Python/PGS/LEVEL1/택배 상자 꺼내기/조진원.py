def solution(n, w, num):
    answer = 0 # num을 찾기 위해 꺼내는 원소의 총 개수

    boxes = [[] for _ in range(w)] # w개의 빈 상자 생성

    idx = 0 # 현재 원소를 넣을 상자 인덱스
    i = True # True: 인덱스 증가 방향, False: 인덱스 감소 방향
    for ns in range(1,n+1) : # 1부터 n까지의 숫자를 각 상자에 지그재그로 분배
        boxes[idx].append(ns) # 현재 상자에 숫자 추가
        if i : # 인덱스 증가 방향
            idx += 1 # 다음 상자로 이동
            if idx == w : # 마지막 상자를 넘어가면
                idx -= 1 # 마지막 상자로 되돌리고
                i = False # 방향을 감소로 변경
        else : # 인덱스 감소 방향
            idx -= 1 # 이전 상자로 이동
            if idx < 0 : # 첫 번째 상자보다 작아지면
                idx += 1 # 첫 번째 상자로 되돌리고
                i = True # 방향을 증가로 변경

    for box in boxes : # 각 상자를 순회
        if num in box : # 현재 상자에 num이 있다면
            p = 0 # 꺼낸 원소를 저장할 변수
            while p != num : # num을 찾을 때까지 반복
                p = box.pop() # 상자에서 마지막 원소를 꺼냄
                answer += 1 # 꺼낸 원소 개수 증가
        else : # num이 없으면
            pass # 다음 상자로 넘어감
    return answer
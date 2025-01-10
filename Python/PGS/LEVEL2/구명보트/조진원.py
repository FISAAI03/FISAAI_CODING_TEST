from collections import deque

def solution(people, limit):
    # 정렬
    people.sort()
    
    # 큐 변환
    people = deque(people)
    
    # 초기값 설정
    answer = 0
    
    # people 리스트를 비울때까지 반복
    while len(people) > 0 :
        # 맨 뒤에 가장 큰 값을 먼저 뽑는다.
        k = people.pop()
        
        # people 리스트가 비어버렸으면 break
        if len(people) == 0 :
            answer += 1
            break
            
        # 가장 무거운 사람과 가장 가벼운 사람을 조합해서 limit보다 작으면 합침
        elif k + people[0] <= limit :
            people.popleft()
        
        # 그 외의 경우는 한명만 보냄
        answer += 1
        
    return answer
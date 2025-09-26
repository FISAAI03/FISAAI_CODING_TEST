from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    
    # course 배열에 있는 숫자(c)마다 반복 → 코스 요리의 메뉴 개수를 의미
    for c in course:
        sub = []  # 해당 코스 개수로 뽑은 모든 조합을 담을 리스트
        
        # 각 손님의 주문을 순회
        for order in orders:
            # 주문 문자열을 정렬한 뒤, c개씩 조합 생성
            # 예: order = "CBA", c=2 → ('A','B'), ('A','C'), ('B','C')
            for comb in combinations(sorted(order), c):
                sub.append(''.join(comb))  # tuple → 문자열로 변환 후 추가
        
        # 각 조합이 몇 번 등장했는지 세기
        counter = Counter(sub)
        
        # counter가 비어 있다면(해당 코스 길이의 조합이 아예 없음) 건너뜀
        if not counter:
            continue
        
        # 가장 많이 주문된 횟수(최대 빈도수) 찾기
        max_order = max(counter.values())
        
        # 한 번만 나온 조합은 조건(최소 2명 이상 주문)에 맞지 않으므로 제외
        if max_order == 1:
            continue
        
        # 가장 많이 주문된 조합들을 answer에 추가
        for order, count in counter.items():
            if count == max_order:
                answer.append(order)
    
    # 모든 코스 요리 후보를 사전순으로 정렬하여 반환
    return sorted(answer)

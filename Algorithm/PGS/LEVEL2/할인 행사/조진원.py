from collections import Counter

def solution(want, number, discount):

    # 상품 목록과 개수를 dictionary화
    product = dict()
    for w, n in zip(want, number) :
        product[w] = n
        
    
    answer = 0
    for idx in range(len(discount)-9) :
        
        # 10개씩 슬라이싱 해서 Counter 함수를 써서 product와 같으면 하나를 증가시킨다.
        if Counter(discount[idx:idx+10]) == product :
            answer += 1
            
    return answer
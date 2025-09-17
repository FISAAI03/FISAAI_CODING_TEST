from collections import Counter

def solution(topping):
    answer = 0
    
    # 동생 딕셔너리를 완성한다
    bro = Counter(topping)
    
    # 철수 딕셔너리 생성
    me = dict()
    
    # 동생꺼에서 하나 빼서 철수한테 준다. 그리고 딕셔너리의 길이가 일치하면 answer값을 증가시킨다.
    for top in topping :
        
        # 철수
        if top not in me :
            me[top] = 1
        else :
            me[top] += 1
        
        # 동생
        if top in bro :
            bro[top] -= 1
            
            if bro[top] == 0 :
                del bro[top]
        
        if len(me) == len(bro) :
            answer += 1
        
    
    return answer
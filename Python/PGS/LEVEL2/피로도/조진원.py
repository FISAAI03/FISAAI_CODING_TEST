from itertools import permutations

# 던전이 8개밖에 안되니 완전탐색

def solution(k, dungeons):
    answer = 0
    # 순열 활용    
    for perm in permutations(dungeons) :
        # 값 생성
        ans = 0
        # 피로도 초기화
        t = k
        for [i,j] in perm :
            # 피로도가 최소피로도 보다 높으면 카운트하기
            if t >= i :
                t -= j
                ans += 1
            else :
                pass
            
        # 횟수가 기존것보다 크면 반영
        answer = max(ans,answer)
        
    return answer
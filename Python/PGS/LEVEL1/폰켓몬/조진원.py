def solution(nums):
    # 중복없이 있는 폰켓몬 개수
    s1 = len(set(nums))
    
    # N/2 마리 수
    s2 = len(nums) // 2
    
    return min(s1,s2)
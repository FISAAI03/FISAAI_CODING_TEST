def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees :
        result = ""
        for s in tree :
            if s in skill :
                result += s
        
        if skill[:len(result)] == result :
            answer += 1
            
    return answer
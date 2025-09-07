def solution(scores):
    answer = 0
    for score in scores :
        min_score = float('inf')
        max_score = 0

        sum_score = 0
        for s in score :
            min_score = min(min_score, s)
            max_score = max(max_score, s)
            sum_score += s
        
        final_score = (sum_score - (min_score + max_score)) / (len(score) - 2)

        answer = max(answer, final_score)
    
    return answer

scores = [[85, 92, 95, 90], [91, 76, 85, 50]]

print(solution(scores))
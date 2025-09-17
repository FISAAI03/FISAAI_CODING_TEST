def solution(projects) :
    answer = []

    projects = sorted(projects, key = lambda x : (-x[1], -x[2]))

    for a,b,c in projects :
        answer.append(a)
    return answer



projects = [[5, 90, 90], [1, 90, 70], [3, 95, 70], [2, 85, 85], [4, 70, 90]]  

print(solution(projects))
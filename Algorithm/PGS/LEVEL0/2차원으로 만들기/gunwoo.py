def solution(num_list, n):
    answer = [[]]
    for i in range(0,int(len(num_list)), n):
        answer.append(num_list[i:i+n])
    answer.pop(0)
    return answer
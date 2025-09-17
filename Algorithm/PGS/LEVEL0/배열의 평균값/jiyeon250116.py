def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer

# mean은 numpy를 호출해야하는데, 코테에는 numpy 호출이 불가함. 그냥 sum/ len으로 구할 것

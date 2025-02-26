def solution(s):
    numbers = list(map(int, s.split(' ')))
    min_number = min(numbers)
    max_number = max(numbers)
    return str(min_number) + ' ' + str(max_number)
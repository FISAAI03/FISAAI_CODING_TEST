def solution(n):
    answer = 0
    arr = [i for i in range(1 ,n + 1)]

    start = 0
    end = 1

    while start < n:
        if sum(arr[start:end]) == n:
            answer += 1
            start += 1
        elif sum(arr[start:end]) < n:
            end += 1
        else:
            start += 1
    return answer
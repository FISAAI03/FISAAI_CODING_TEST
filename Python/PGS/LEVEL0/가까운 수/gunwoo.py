def solution(array, n):
    arr = []
    array.sort()
    for i in array:
        arr.append(abs(i-n))
    b = arr.index(min(arr))
    answer = array[b]
    return answer
def solution(arr, idx):
    answer = 0
    newarr = arr[::-1]
    b = len(arr)-newarr.index(1)-1
    if b >= idx:
        answer = b
    else:
        answer = -1
    return answer
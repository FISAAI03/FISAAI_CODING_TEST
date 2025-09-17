import numpy as np

def solution(arr1, arr2):
    arr1 = np.matrix(arr1)
    arr2 = np.matrix(arr2)
    answer = arr1 * arr2
    return answer.tolist()
def solution(arr):
    answer = []
    cnt = arr.count(2)
    if cnt == 1:
        
        answer = [2]
        
    elif cnt == 0:
        answer = [-1]
        
    else:
        b = arr[::-1]
        answer = arr[arr.index(2): len(b)-b.index(2)]
            
    
    return answer
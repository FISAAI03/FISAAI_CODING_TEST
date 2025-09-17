def solution(n):
    answer = ""
    while n > 0:
        n -= 1
        an = n%3
        n = n//3
        
        if an == 0:
            answer = "1" + answer
        elif an == 1:
            answer = "2" + answer
        elif an == 2:
            answer = "4" + answer
                      
    return answer
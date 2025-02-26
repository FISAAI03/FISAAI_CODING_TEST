# 스택/큐로 푼다
# 결국은 새로 들어온 값이랑 직전 값이랑 만나면 없어지는건 원리는 똑같음

def solution(s):
    stack = []
    for char in s :
        if len(stack) == 0 :
            stack.append(char)
        elif stack[-1] == char :
            stack.pop()
        else :
            stack.append(char)
            
    if len(stack) == 0 :
        return 1
    else :
        return 0
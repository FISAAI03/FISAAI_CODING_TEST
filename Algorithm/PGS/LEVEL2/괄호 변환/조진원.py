def solution(s):
    n = len(s)
    
    s = list(s*2)
    answer = 0
    for i in range(n) :
        stack = []
        part = s[i:i+n]
        while part :
            k = part.pop()
            if len(stack) == 0 :
                stack.append(k)
            elif stack[-1] == ']' and k == '[' :
                stack.pop()
            elif stack[-1] == '}' and k == '{' :
                stack.pop()
            elif stack[-1] == ')' and k == '(' :
                stack.pop()
            else :
                stack.append(k)
        if len(stack) == 0 :
            answer += 1
    return answer
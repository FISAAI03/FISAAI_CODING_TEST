def solution(s):
    answer = True

    stack = []
    if s[0] == ')' or s[-1] == '(':
        answer = False
        return answer

    for idx in range(len(s)):
        if s[idx] == ')':
            if len(stack) == 0:
                answer = False
                return answer
            elif stack[-1] == '(':
                stack.pop()
        else:
            stack.append(s[idx])

    if len(stack) == 0:
        answer = True
    else:
        answer = False

    return answer
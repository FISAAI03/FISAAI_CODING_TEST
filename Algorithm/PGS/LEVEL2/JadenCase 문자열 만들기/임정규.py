def solution(s):
    answer = ''
    space_flag = True
    for idx in range(len(s)):
        if s[idx] == ' ':
            space_flag = True
            answer += s[idx]
            continue
        if space_flag == True:
            answer += s[idx].upper()
            space_flag = False
        else:
            answer += s[idx].lower()
    return answer
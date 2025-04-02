while 1:
    stack = []
    flag = True
    st = input()
    if st == '.':
        break
    for s in st:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1]=="(":
                stack.pop()
            else:
                flag = False
                break
        elif s == "]":
            if stack and stack[-1]=="[":
                stack.pop()
            else:
                flag = False
                break
    if flag and not stack:
        print('yes')
    else:
        print('no')
    
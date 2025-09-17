t = int(input())
ans = []

for _ in range(t):
    # VPS는 첫 문자가 "("로 시작해야만 하기 때문에 미리 첫 문자 스택에 삽입
    stack = ["("]

    ps = input()

    # 첫 괄호와 끝 괄호를 확인하여 VPS가 아닌 케이스 미리 거름
    if (ps[0] == ")") or (ps[-1] == "("):
        ans.append("NO")
    else:
        # 첫 문자는 스택에 미리 넣어두어서 두 번째 문자부터 차례로 확인
        for i in ps[1:]:
            # 스택이 비어있지 않고(스택의 원소는 "("로 구성되어 있음) "()" 괄호가 완성되는지 확인
            if stack and i == ")":
                # 스택에 "("이 존재한다면 완전한 괄호가 완성되기에 "(" 원소를 스택에서 팝
                stack.pop()
            # 스택이 비어있고(스택의 첫 "("값은 이미 괄호가 완성되어 팝된 상태) ")" 값이 나올 경우 확인
            elif not stack and i == ")":
                # stack.append(i)을 실행한다면 스택은 [")"] => vps가 아님님
                stack.append(i)
                break
            else:
                # 그 외 ps안의 i값은 "("
                stack.append(i)

        # for문을 모두 돌았을 경우 혹은 break로 빠져나왔을 때, stack이 비어있으면 YES, 아니면 NO
        if not stack:
            ans.append("YES")
        else:
            ans.append("NO")

for x in ans: print(x)
import sys

input = sys.stdin.readline

s = input().strip()
es = input().strip()
stack = []

# stack을 활용하여 s문자열의 문자 하나씩 쌓으면서 es 문자가 확인됐을 때마다, pop해줌
for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-len(es):]) == es:
        for _ in range(len(es)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')

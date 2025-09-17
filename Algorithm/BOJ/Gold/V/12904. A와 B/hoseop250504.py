s = input()
t = input()

# A연산 거꾸로 수행 함수
def A(str):
    return str[:-1]

# B연산 거꾸로 수행 함수
def B(str):
    return str[:-1][::-1]

res = 0
# t문자열을 뒤에서 A, B연산을 거꾸로 수행, TOP-DOWN 방식 사용하여 s문자열과 비교
while len(t) >= len(s):
    if s == t:
        res = 1
        break
    elif t[-1] == 'A':
        t = A(t)
    elif t[-1] == 'B':
        t = B(t)

print(res)
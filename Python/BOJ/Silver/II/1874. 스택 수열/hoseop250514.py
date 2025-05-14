n = int(input())

seq = []
for _ in range(n):
    seq.append(int(input()))

# 1~n까지 숫자 저장 스택
stack_in = []
# 연산 저장 리스트
operation = []
num = 1
for i in seq:
    # 수열 숫자가 num 보다 작고, 스택 마지막 원소가 i와 같을 경우 팝, 아니면 입력 수열 생성 불가능하므로 break
    if num > i:
        if stack_in[-1] == i:
            stack_in.pop()
            operation.append('-')
        else:
            break
    
    # i가 num 보다 작을 경우, stack을 쌓고 연산 추가가
    while num <= i:
        stack_in.append(num)
        operation.append('+')
        if num == i:
            stack_in.pop()
            operation.append('-')
        num += 1
        
# stack이 비어있지 않으면(break를 만났을 경우), no 출력
if stack_in:
    print('NO')
else:
    for op in operation:
        print(op)

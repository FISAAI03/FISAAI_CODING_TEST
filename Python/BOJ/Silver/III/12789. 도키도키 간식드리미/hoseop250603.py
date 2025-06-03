from collections import deque

n = int(input())

# 큐와 스택을 활용하여 stack에 값이 존재한다면 순서대로 통과 불가능
queue = deque(list(map(int, input().split())))
stack = []

# i값을 n까지 순서대로 올리면서 그 값에 맞는 큐와 스택안의 값을 빼오는 코드
i = 1
while stack or queue:
    if queue and queue[0] == i:
        queue.popleft()
        i += 1
    elif stack and stack[-1] == i:
        stack.pop()
        i += 1
    else:
        if queue:
            stack.append(queue.popleft())
        else:
            # i값을 뽑을 수 없는 상태라면 while문을 빠져나옴옴
            break

# stack에 불완전한 순서로 정렬된 값들이 있다면(순서대로 간식받기 불가능) Sad 출력
# 순서대로 모두 간식을 받았다면(큐와 스택에 학생이 없을 경우) Nice 출력
if stack:
    print('Sad')
else:
    print('Nice')
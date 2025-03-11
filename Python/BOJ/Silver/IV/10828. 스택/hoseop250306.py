import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    order = sys.stdin.readline().strip()

    if 'push' in order:
        stack.append(int(order.split()[-1]))
    elif order == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
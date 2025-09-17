from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

dq = deque([])
for _ in range(n):
    cmd = input().strip().split()
    if cmd[0] == 'push_front':
        dq.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        dq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        print(dq.popleft()) if dq else print(-1)
    elif cmd[0] == 'pop_back':
        print(dq.pop()) if dq else print(-1)
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        print(1) if not dq else print(0)
    elif cmd[0] == 'front':
        print(dq[0]) if dq else print(-1)
    elif cmd[0] == 'back':
        print(dq[-1]) if dq else print(-1)
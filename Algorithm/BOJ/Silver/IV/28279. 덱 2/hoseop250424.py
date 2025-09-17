from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

dq = deque([])
for _ in range(n):
    cmd = input().strip().split()
    if cmd[0] == '1':
        dq.appendleft(cmd[1])
    elif cmd[0] == '2':
        dq.append(cmd[1])
    elif cmd[0] == '3':
        print(dq.popleft()) if dq else print(-1)
    elif cmd[0] == '4':
        print(dq.pop()) if dq else print(-1)
    elif cmd[0] == '5':
        print(len(dq))
    elif cmd[0] == '6':
        print(1) if not dq else print(0)
    elif cmd[0] == '7':
        print(dq[0]) if dq else print(-1)
    elif cmd[0] == '8':
        print(dq[-1]) if dq else print(-1)
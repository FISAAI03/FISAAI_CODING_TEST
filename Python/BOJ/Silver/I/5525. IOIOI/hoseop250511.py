import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

p_n = "I"+"OI"*n
cnt = 0
i = 0
if m < (n*2 + 1):
    print(cnt)
else:
    while i <= m - (n*2+1):
        if s[i] != 'O' and s[i:n*2+1+i] == p_n:
            cnt += 1
            i += n*2+1
            while i <= m-2:
                if s[i:i+2] == 'OI':
                    cnt += 1
                    i += 2
                else:
                    i -= 1
                    break
        else:
            i += 1
    print(cnt)
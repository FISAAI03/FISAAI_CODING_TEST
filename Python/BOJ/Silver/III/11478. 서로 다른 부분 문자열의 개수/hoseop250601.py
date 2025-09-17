import sys

input = sys.stdin.readline

st = input().strip()

sub_st = set()

for i in range(len(st)):
    for j in range(i, len(st)):
        if st[i:j+1] not in sub_st:
            sub_st.add(st[i:j+1])

print(len(sub_st))
import sys
from math import ceil, log
from collections import defaultdict

# 트리 초기화 함수
def init(node, start, end):
    if start == end:
        tree[node] = 1
        return
    
    mid = (start + end) // 2
    init(2*node, start, mid)
    init(2*node + 1, mid + 1, end)
    tree[node] = tree[2*node] + tree[2*node + 1]

# 구간 값 구하기 함수
# node = 현재 트리의 인덱스 번호, (start, end) = 현재 node 범위, idx = 해당 인덱스 까지의 구간합
def query(node, start, end, idx):
    # 요청 범위가 벗어나는 경우 0을 리턴
    if idx < start:
        return 0
    # 요청 범위 안에 완전히 들어왔을 때
    if 0 <= start and end <= idx:
        return tree[node]
    
    mid = (start + end) // 2
    q1 = query(2*node, start, mid, idx)
    q2 = query(2*node + 1, mid + 1, end, idx)
    
    return q1 + q2

# 업데이트 합수
def update(node, start, end, idx):
    if idx < start or end < idx:
        return
    
    tree[node] -= 1

    if start != end:
        mid = (start + end) // 2
        update(2*node, start, mid, idx)
        update(2*node + 1, mid + 1, end, idx)

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

# 각 수의 기존 인덱스를 저장할 hash맵 생성
hash = defaultdict(list)
for i, j in enumerate(a):
    hash[j].append(i)

# 내림차순 정렬 (큰 수 부터 탐색색)
a = sorted(set(a), reverse=True)

H = ceil(log(n, 2))
size = pow(2, H) * 2
tree = [0] * size

init(1, 0, n-1)


cnt = 0
i = 0
for j in a:
    # 겹치는 같은 수가 있을 경우, 큰 인덱스 부터 작은 인덱스 순으로 for문 처리
    for k in sorted(hash[j], reverse=True):
        idx = k
        # 트리의 해당 인덱스 값 업데이트
        update(1, 0, n-1, idx)
        # 트리 구간합을 통해 바뀐 인덱스 값 도출
        updated_idx = query(1, 0, n-1, idx)
        # a값을 탐색 할때마다 큰 수는 맨 뒤로 가서 위치가 고정 되며, 하나씩 빠지게 됨.
        # 그래서 업데이트 된 인덱스에서 i를 빼면 swap 개수가 나옴
        cnt += n-1 - updated_idx - i
        i += 1

print(cnt)
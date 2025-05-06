import sys
from math import ceil, log

# 트리 초기화
# node = 현재 노드 번호, start = 트리 시작 인덱스, end = 트리 끝 인덱스
def init(node, start, end): 
    if start == end:
        tree[node] = 1
        return
    
    mid = (start + end) // 2
    init(2*node, start, mid)
    init(2*node + 1, mid + 1, end)
    tree[node] = tree[2*node] + tree[2*node + 1]

# 구간 값 구하기 함수
# node = 현재 트리의 인덱스 번호, (start, end) = 현재 node 범위, (left, right) = 요청 범위
# def query(node, start, end, left=0, right):
#     # 요청 범위가 벗어나는 경우 0을 리턴
#     if right < start or end < left:
#         return 0
#     # 요청 범위 안에 완전히 들어왔을 때
#     if left <= start and end <= right:
#         return tree[node]
    
#     mid = (start + end) // 2
#     q1 = query(2*node, start, mid, left, right)
#     q2 = query(2*node + 1, mid + 1, end, left, right)
    
#     return q1 + q2

# 값을 넣을 수 있는 위치값 반환
def query(node, start, end, ai):
    # 위치를 찾는 동시에 즉시 update
    tree[node] -= 1
    # 위치 반환
    if start == end:
        return end
    
    mid = (start + end) // 2
    # 왼쪽 자식 노드값이 ai보다 크면, 가용한 위치가 왼쪽에 있다는 뜻으로 재귀
    # 아니라면, 오른쪽 자식 노드값으로 이동하여 ai값과 오른쪽 자식 노드값 차이로 재귀귀
    if tree[node*2] > ai:
        return query(node*2, start, mid, ai)
    else:
        return query(node*2 + 1, mid+1, end, ai-tree[node*2])

# 특정 노드 값 업데이트 함수
# idx = 업데이트할 값의 인덱스, diff = 기존 값과의 차이
def update(node, start, end, idx, diff):
    if idx < start or end < idx:
        return
    
    tree[node] += diff

    if start != end:
        mid = (start + end) // 2
        update(2*node, start, mid, idx, diff)
        update(2*node+1, mid+1, end ,idx, diff)

input = sys.stdin.readline
n = int(input())

# 2**k >= N을 만족하는 k의 최솟값으로 2**k*2를 트리 배열 크기로 정의
H = ceil(log(n, 2))
size = pow(2, H) * 2
tree = [0] * size

init(1, 0, n-1) # 1번 노드가 0부터 n-1의 범위를 가지고 있다는 뜻

seq = [0]*(n)
for i in range(1, n+1):
    ai = int(input())
    idx = query(1, 0, n-1, ai)
    seq[idx] = i

for x in seq:
    print(x)

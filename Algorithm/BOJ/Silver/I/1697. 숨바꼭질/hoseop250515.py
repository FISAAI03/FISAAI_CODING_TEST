from collections import deque

n, k = map(int, input().split())

# 나누기 연산을 queue를 활용해 수행하면서 n과 제일 가까워 질 때까지 2로 나누기
def bfs(n, k):
    cnt = 0
    queue = deque([[k, cnt]])
    while abs(n-(queue[0][0])) > abs(n-(queue[0][0]//2)):
        k2 = queue.popleft()
        if k2[0]%2 == 0:
            queue.append([k2[0]//2, k2[1]+1])
            
        else:
            queue.append([(k2[0]+1)//2, k2[1]+2])
            queue.append([(k2[0]-1)//2, k2[1]+2])
    return queue

# k가 n보다 크면 bfs함수를 통해 n과 제일 가까운 숫자들의 집합 중 가장 빠른 시간을 계산함함
if n < k:
    eta = 100000
    if n == 0:
        for q in bfs(1, k):
            sec = abs(1-q[0]) + q[1]
            if sec < eta:
                eta = sec
        print(eta + 1)
    else:
        for q in bfs(n, k):
            sec = abs(n-q[0]) + q[1]
            if sec < eta:
                eta = sec
        print(eta)
    
# n이 k보다 더 작을 경우, 차이를 출력력
else:
    print(n-k)
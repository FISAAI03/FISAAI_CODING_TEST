# 한쪽은 최소값, 한쪽은 최대값을 뽑아내는 형식으로 최소값을 구한다.


from collections import deque

def solution(A,B):
    # 정렬 후, 큐 형태로 변환
    A = deque(sorted(A))
    B = deque(sorted(B))
    
    answer = 0
    # A 최소값 * B 최대값과 A 최대값 * B 최소값을 비교한다.
    while A :
        if A[0] * B[-1] > A[-1] * B[0] :
            answer += A.popleft() * B.pop()
        else :
            answer += A.pop() * B.popleft()

    return answer
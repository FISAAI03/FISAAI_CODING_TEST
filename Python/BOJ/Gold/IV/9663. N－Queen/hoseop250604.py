'''
백트래킹을 활용하여 보드를 돌며 퀸을 놓는 방법
x-y => 보드에서 해당 위치의 인덱스를 빼면 오른쪽 대각선의 동일한 값들이 나옴(오른쪽 대각선 방문 위치 확인 가능)
x+y => 보드에서 해당 위치의 인덱스를 더하면 왼쪽 대각선의 동일한 값들이 나옴(왼쪽 대각선 방문 위치 확인 가능)
※ 왼쪽 대각선, 오른쪽 대각선, 컬럼 방문 세트 총 3개를 독립적으로 방문 확인인
'''

def backtrack(x):
    global cnt

    if x == n:
        cnt += 1
        return
    
    for y in range(n):
        if y not in col and x-y not in right_diag and x+y not in left_diag:
            col.add(y)
            right_diag.add(x-y)
            left_diag.add(x+y)
            backtrack(x+1)
            col.remove(y)
            right_diag.remove(x-y)
            left_diag.remove(x+y)

n = int(input())

right_diag = set()
left_diag = set()
col = set()
cnt = 0

backtrack(0)
print(cnt)
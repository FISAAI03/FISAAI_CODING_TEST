n, m = map(int, input().split())

A = [list(input()) for _ in range(n)]
B = [list(input()) for _ in range(n)]

# 행렬 A, B가 3보다 작을 경우
if (n < 3) or (m < 3):
    # 행렬 A ,B가 다를 경우
    if A != B:
        print(-1)
    # 같을 경우
    else:
        print(0)

else: 
    cnt = 0
    # 행렬 A의 각 원소 하나씩 돌면서 B의 같은 위치의 값이 다르면 3X3크기 만큼 값을 바꿔줌
    for i in range(n-2):
        for j in range(m-2):
            if A[i][j] != B[i][j]:
                cnt += 1
                for x in range(3):
                    for y in range(3):
                        if A[i+x][j+y] == "1":
                            A[i+x][j+y] = "0"
                        else:
                            A[i+x][j+y] = "1"
        # for j 문이 끝난 시점에 해당 행(i)의 전체 리스트 값이 다르면 -1 반환
        if A[i] != B[i]:
            cnt = -1
            break
    # 모든 원소를 돌았을 때, 전체 A, B 행렬이 다를 경우 -1 반환
    if A != B:
        cnt = -1

    print(cnt)
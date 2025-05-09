import sys

input = sys.stdin.readline

n = int(input())

identity_mat = [[1, 0], [0, 1]]

def dot(m1, m2): 
    m = [[(m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0]) % 1000000007,
        (m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]) % 1000000007],
        [(m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0]) % 1000000007,
        (m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]) % 1000000007]]
    return m

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
# 행렬 거듭제곱을 활용한 분할 정복
# [f(n), f(n-1)] = [[1, 1], [1, 0]]**(n-1) X [f(1)=1, f(0)=0]
def fibo_mat(n):
    mat = [[1, 1],[1, 0]]
    if n == 0:
        return identity_mat
    elif n == 1:
        return mat
    else:
        e = 1
        while pow(2, e) <= n:
            mat = dot(mat, mat)
            e += 1
        return dot(mat, fibo_mat(n-pow(2, e-1)))


print(fibo_mat(n-1)[0][0])
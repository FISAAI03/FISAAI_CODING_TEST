n, k = map(int, input().split())

# 초기 무게와 가치를 저장할 리스트 생성
wv_lst = [[0, 0]]

# 입력받은 무게와 가치 값을 리스트로 wv_lst에 저정함
for _ in range(n):
    wv_lst.append(list(map(int, input().split())))

# 초기 가치를 저장할 리스트 생성
dp = [[0] * (k+1) for _ in range(n+1)]

# dp 리스트 행렬 사이즈에 맞게 for믄을 돌며 최적 가치값을 할당함함
for i in range(1, n+1):
    weight = wv_lst[i][0]
    value = wv_lst[i][1]
    for j in range(1, k+1):
        # 현재 넣을 수 있는 무게(j)가 입력받은 무게(weight)보다 작을 경우(==가방에 넣지 못할 경우), 이전 가치값을 할당
        if j < weight:
            dp[i][j] = dp[i-1][j]
        # j가 weight보다 클 경우(==가방에 물건을 넣을 수 있을 경우), 이전 값과 이전 물건에서 (현재 넣을 수 있는 무게 - 이전 물건 무게) + 가치 중 최댓값을 선택
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

# dp[n][k]가 최댓값이 됨됨
print(dp[n][k])
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    rank = []
    for _ in range(N):
        rank.append(list(map(int, input().split())))

    # 서류 순위로 정렬
    rank.sort(key=lambda x: x[0])

    cnt = 1
    # 서류 1등의 면접 순위를 max로 할당
    max_ = rank[0][1]
    for i in range(1, N):
        # 면접 등수가 max_값보다 작은(순위가 높은) 값이 있다면 면접 등수를 갱신 및 합격 인원수 +1
        if max_ > rank[i][1]:
            max_ = rank[i][1]
            cnt += 1

    print(cnt)
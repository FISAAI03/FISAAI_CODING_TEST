n = int(input())
ans = [1]

if n > 1:
    for i in range(2, n+1):
        # 마지막 값(== 1) 인덱스를 자식 노드 인덱스로 저장
        child = len(ans) -1
        while child > 0:
            # 힙 정의에 따른 부모 노드 인덱스 저장
            parent = (child - 1) // 2
            # 1값을 위로 보내기 위해 스왑
            ans[parent], ans[child] = ans[child], ans[parent]
            # 부모 인덱스를 자식 인덱스로 다시 할당하여 1값이 최상단에 위치할 때까지 위 과정 반복
            child = parent

        # 최대값 i를 append하여 최상단에 위치한 1값과 바꿔줌으로써 ans 완성
        ans.append(i)
        ans[0], ans[-1] = ans[-1], ans[0]

print(*ans)
def solution(arr):
    count = [0, 0]  # 0과 1의 개수를 저장하는 리스트
    n = len(arr)  # 배열의 크기

    def compress(x, y, size):
        # 현재 영역의 첫 번째 값 저장
        initial_value = arr[x][y]
        is_same = True  # 모든 값이 동일한지 확인하는 변수

        # 영역 내의 값이 동일한지 검사
        for row in range(x, x + size):
            for col in range(y, y + size):
                if arr[row][col] != initial_value:
                    is_same = False
                    break  # 다른 값이 발견되면 반복 중지
            if not is_same:
                break

        # 모든 값이 동일하면 해당 숫자의 개수 증가
        if is_same:
            count[initial_value] += 1
        else:
            # 영역을 4개로 나누어 재귀적으로 검사
            half = size // 2
            compress(x, y, half)  # 왼쪽 위
            compress(x + half, y, half)  # 오른쪽 위
            compress(x, y + half, half)  # 왼쪽 아래
            compress(x + half, y + half, half)  # 오른쪽 아래

    # 전체 배열을 압축 시작
    compress(0, 0, n)
    
    return count
def factory(n):
    a = 1
    for i in range(1, n + 1):   # 1부터 n까지 곱해서 팩토리얼 계산
        a *= i
    return a

def solution(n, k):
    answer = []                          # 결과를 담을 리스트
    arr = [i for i in range(1, n + 1)]   # 아직 선택되지 않은 숫자들

    for _ in range(n):
        if len(arr) == 1:        # 마지막 숫자 하나만 남았을 경우
            answer.append(arr.pop())
            break

        # (len(arr)-1)! : 현재 자리에서 한 숫자를 고른 뒤 남은 경우의 수
        s = factory(len(arr) - 1)

        # k번째 순열이 몇 번째 블록(= 몫)에 속하는지
        idx = k // s
        # 블록 내에서 몇 번째인지(= 나머지)
        step = k % s
        # k를 업데이트해서 다음 자리 계산에 사용
        k = step

        if step != 0:
            # 아직 블록 안에서 순열이 더 남아있을 때
            # 현재 블록의 시작 인덱스를 pop
            answer.append(arr.pop(idx))
        else:
            # 정확히 블록의 끝에 해당할 때 (나머지 0)
            # 앞자리까지는 idx-1번째 원소를 쓰고,
            # 뒤의 원소들은 역순으로 이어붙이면 k번째 순열 완성
            answer.append(arr.pop(idx-1))
            answer += arr[::-1]   # 남은 원소들 역순으로 붙이기
            break

    return answer
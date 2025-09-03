import math

def solution(n, k):
    # 사용할 숫자들을 리스트에 저장 (1 ~ n)
    numbers = [num for num in range(1, n+1)]
    result = []
    
    # numbers가 빌 때까지 반복
    while numbers:
        # 현재 자리에서 한 숫자를 고정했을 때 만들 수 있는 경우의 수 (남은 숫자-1)!
        block_size = math.factorial(len(numbers)-1)
        
        # k번째 순열에서 현재 자리 숫자의 인덱스 결정
        index = (k-1) // block_size
        
        # 다음 자리를 위한 k 갱신
        k = k % block_size
        if k == 0:
            k = block_size
        
        # 선택된 숫자를 결과에 추가하고, numbers에서 제거
        result.append(numbers.pop(index))
    
    # 최종적으로 k번째 순열을 담은 리스트 반환
    return result
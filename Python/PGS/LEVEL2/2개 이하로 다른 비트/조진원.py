# 1 10 11 101 110 0111 1011 1101 1110 1111


def solution(numbers):
    answer = []
    
    for number in numbers :
        # 이진수 변환
        x = bin(number)[2:]
        # 제일 오른쪽에 있는 0위치 찾기
        zero_index = x.rfind('0')
        
        # 0이 없으면
        if zero_index == -1 :
            k = '10' + '1'*(len(x)-1)
            
        # 끝자리에 있으면 끝자리를 1로 바꾸기
        elif zero_index == len(x)-1 :
            x_list = list(x)
            x_list[zero_index] = '1'
            k = ''.join(x_list)
        
        # 그렇지 않으면 0과 오른쪽 1과 위치 바꾸기
        else :
            x_list = list(x)
            x_list[zero_index] = '1'
            x_list[zero_index+1] = '0'
            k = ''.join(x_list)
        
        # 십진수 변환환
        answer.append(int(k,2))
    return answer
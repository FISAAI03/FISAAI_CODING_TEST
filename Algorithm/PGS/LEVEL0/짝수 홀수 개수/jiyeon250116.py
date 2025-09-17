def solution(num_list):
    answer = [0,0]
    for i in num_list:
        if i % 2 == 0: 
            answer[0] += 1
        elif i % 2 == 1:
            answer[1] += 1
    return answer
## 빈리스트 answer = [] 으로 설정하고 시작하면, answer[0]과 answer[1]을 인식할 수 없음.
## answer 리스트는 빈 리스트[]로 초기화 되어 있기 때문에 answer[0]과 answer[1]에 접근하면 인덱스 오류가 발생하기 때문.
## 해결 방법: answer 리스트를 [0, 0]으로 초기화해야 함.


# sol 2
def solution(num_list):
    answer = [0, 0]  # [짝수 개수, 홀수 개수]
    for n in num_list:  # 리스트의 각 숫자를 순회
        answer[n % 2] += 1  # n % 2 결과로 짝수/홀수를 구분하여 카운트 증가
    return answer


# LRU : 가장 최근에 사용되지 않은 데이터를 지우고 그것을 채우는 것

def solution(cacheSize, cities):
    # 초기값
    answer = 0
    
    # 메모리는 딕셔너리로
    memory = dict()
    
    # cacheSize가 0이면 바로 * 5
    if cacheSize == 0 :
        return len(cities) * 5
    
    for num, city in enumerate(cities):
        # 소문자로 바꾸기
        city = city.lower()
        
        # cache hit
        if city in memory:
            memory[city] = num
            answer += 1
            
        # cache miss
        else:
            # 메모리가 다 차지 않았으면 추가
            if len(memory) < cacheSize:
                memory[city] = num
                answer += 5
            # 메모리가 찰 경우
            else:
                # 최소값 탐색 및 삭제
                min_city = sorted(memory.items(), key=lambda x: x[1])[0][0]
                del memory[min_city]
                
                # 추가
                memory[city] = num
                answer += 5
    
    return answer

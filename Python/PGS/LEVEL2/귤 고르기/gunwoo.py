def solution(k, tangerine):
    answer = 0
    tangerine = sorted(tangerine) # 오름차순 정렬
    bowl = 0
    a = list(set(tangerine)) # 중복값 제거
    a = sorted(a) # 오름차순 정렬
    lst = []
   
    for i in a:
        lst.append(tangerine.count(i))
    lst = sorted(lst, reverse = True) # 각각의 개수를 구한 후 내림차순 정렬
    
     
    for i in lst:
        if k > bowl:
            bowl += i
            answer += 1  #귤값을 더하다가 k 값보다 커질 때까지 answer에 1을 더해줌
            
    return answer



# 처음에 위와 같이 코드를 짰다. 이렇게 되니 테스트케이스 32개중 28개만 맞추고 나머지는 시간초과가 났다 이에 dictionary를 활용하여 코드를 짰다.



def solution(k, tangerine):
    answer = 0
    tangerine = sorted(tangerine)
    bowl = 0
    a = list(set(tangerine))
    a = sorted(a)
    cdic = {}

    for i in tangerine:
        if i in cdic:
            cdic[i] += 1
        else:
            cdic[i] =1
            
    lst = list(cdic.values())
    
    lst = sorted(lst, reverse = True)
     
    for i in lst:
        if k > bowl:
            bowl += i
            answer += 1
            
    return answer

# dictionary를 사용하면 시간초과가 나지 않는다
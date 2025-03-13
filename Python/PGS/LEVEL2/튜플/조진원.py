def solution(s):
    answer = []
    
    # 중괄호 없애기
    tups = s[2:-2].split('},{')
    
    # 리스트로 재구조화
    re_tup = []
    for tup in tups :
        chk = list(map(int, tup.split(',')))
        re_tup.append(chk)
    
    # 길이 순서대로 정렬
    re_tup = sorted(re_tup, key = lambda x : len(x))
    
    # 짧은 것 부터 하나씩 추가하면서, 없으면 정답리스트에 넣기
    for a in re_tup :
        for b in a :
            if b not in answer :
                answer.append(b)
    return answer
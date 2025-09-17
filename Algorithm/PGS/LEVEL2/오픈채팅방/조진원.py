def solution(record):
    nickname = dict()
    
    # 최종 닉네임 탐색
    for r1 in record :
        if len(r1.split()) == 3 :
            status, user, name = r1.split()
            nickname[user] = name
        else :
            pass
    
    # 정답 들넣기
    answer = []
    for r2 in record :
        if len(r2.split()) == 3 :
            status, user, name = r2.split()
            if status == 'Enter' :
                sentence = nickname[user] + '님이 들어왔습니다.'
                answer.append(sentence)
        
        elif len(r2.split()) == 2 :
            status, user = r2.split()
            if status == 'Leave' :
                sentence = nickname[user] + '님이 나갔습니다.'
                answer.append(sentence)
    
    return answer
def solution(n, words):

    # 말한 횟수를 저장하는 딕셔너리 생성
    chk_dict = dict()
    for i in range(n) :
        chk_dict[i+1] = 0

    # 이전에 언급되었는지 단어를 체크하기
    chk = []
    
    for idx, word in enumerate(words) :
        # 번호 탐색
        num = idx % n + 1
        chk_dict[num] += 1
        
        # # 이전에 말했거나, 끝말잇기가 안되는 거면 끝
        if len(chk) == 0 :
            chk.append(word)
        elif word in chk :
            return [num, chk_dict[num]]
        elif chk[-1][-1] != word[0] :
            return [num, chk_dict[num]]
        else :
            chk.append(word)
    return [0,0]
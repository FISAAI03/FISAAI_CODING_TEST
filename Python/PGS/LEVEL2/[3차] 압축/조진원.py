import string

def solution(msg):
    answer = []
    
    # 길이가 1인 모든 단어를 포함하도록 사전을 초기화
    lzw = dict()
    for idx, char in enumerate(string.ascii_uppercase) :
        lzw[char] = idx+1
        
    # 사전에 현재 입력과 일치하는 가장 긴 문자열 w를 찾기
    
    num = 27
    max_word = 1 # 최대문자열 길이
    
    while len(msg) > 0 :
        x = max_word
        while True :
            w = msg[:x]
            if w in lzw :
                answer.append(lzw[w])
                msg = msg[x:]
                if len(msg) > 0 :
                    wc = w+msg[0]
                    lzw[wc] = num
                    num += 1
                    max_word = max(max_word,len(wc))
                    break
                else :
                    break
            else :
                x -= 1
    
    return answer
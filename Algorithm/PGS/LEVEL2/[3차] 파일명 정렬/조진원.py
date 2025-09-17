def solution(files):
    convert = []
    # 분류하기
    for t, file in enumerate(files) :
        HEAD = ''
        NUMBER = ''
        TAIL = ''
        for idx, char in enumerate(file) :
            if not char.isdigit() :
                HEAD += char
            else :
                break
        
        for idx2, char in enumerate(file[idx:]) :
            if char.isdigit() :
                NUMBER += char
            else :
                break
        
        TAIL += file[(idx+idx2):]
        convert.append((file, HEAD, NUMBER, TAIL, t))
    
    # 정렬하기
    convert = sorted(convert, key = lambda x : (x[1].lower(), int(x[2]), x[4]))
    return [x[0] for x in convert]
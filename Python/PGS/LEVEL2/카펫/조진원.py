def solution(brown, yellow):
    total = brown + yellow
    
    answer = []
    for height in range(3, total) :
        if total % height == 0 :
            width = total // height
            
            for s_height in range(1, yellow + 1) :
                if yellow % s_height == 0 :
                    s_width = yellow // s_height
                    
                    if (width > s_width) & (height > s_height) & ((width - s_width) % 2 == 0) & ((height - s_height) % 2 == 0):
                        answer.append(width)
                        answer.append(height)
                        break
            
            if len(answer) != 0 :
                break
    return answer
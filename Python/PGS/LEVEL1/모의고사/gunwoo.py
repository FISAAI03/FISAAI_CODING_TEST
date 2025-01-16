def solution(answers):
    answer = []
    answer1 = [1,2,3,4,5]
    answer2 = [2,1,2,3,2,4,2,5]
    answer3 = [3,3,1,1,2,2,4,4,5,5]
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(answers)):
        if answers[i] == answer1[i%len(answer1)]:
            count1 +=1
    for i in range(len(answers)):
        if answers[i] == answer2[i%len(answer2)]:
            count2 +=1
    for i in range(len(answers)):
        if answers[i] == answer3[i%len(answer3)]:
            count3 +=1
        
    if count1 > count2 and count1 > count3:
        answer.append(1)
    elif count2 > count1  and count2 > count3:
        answer.append(2)
    elif count3 > count1 and count3 > count2:
        answer.append(3)
    elif count1 == count2 == count3:
        answer.append(1)
        answer.append(2)
        answer.append(3)
    elif count1 == count2 != count3:
        answer.append(1)
        answer.append(2)
    elif count1 != count2 == count3:
        answer.append(2)
        answer.append(3)
    else:
        answer.append(1)
        answer.append(3)
        
    return answer
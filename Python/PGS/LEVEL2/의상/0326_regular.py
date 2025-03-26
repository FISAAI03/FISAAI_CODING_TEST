def solution(clothes):
    answer = 1

    category = {}
    for cloth, cate in clothes:
        if not cate in category:
            category[cate] = [cloth]
        else:
            category[cate].append(cloth)

    for k, v in category.items():
        answer *= (len(v) + 1)

    return answer - 1
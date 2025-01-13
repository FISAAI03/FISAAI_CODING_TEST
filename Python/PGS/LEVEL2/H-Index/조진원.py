'''
1. 핵심은 정렬하는 것,
2. h 값 이상이 h개 이상
3. 정렬한 후, 인덱스를 비교한다.
4.
    6 이상이 1개
    5 이상이 2개
    3 이상이 3개
5. 즉, 인덱스 값과 실제 값이 같아지는 순간을 찾으면 된다.
'''

def solution(citations):
    citations_sort = sorted(citations, reverse=True)
    h = 0
    for i, citation in enumerate(citations_sort) :
        if citation >= (i+1) :
            h = i+1
    return h
from collections import deque

def solution(priorities, location):
    que = deque([n for n in range(len(priorities))])
    priorities = deque(priorities)
    
    answer = []
    while priorities :
        loc = que.popleft()
        p = priorities.popleft()
        
        if max(priorities) > p :
            que.append(loc)
            priorities.append(p)
        else :
            answer.append(loc)
        
        if len(que) == 1 :
            answer.append(que[0])
            break
        
    return answer.index(location) + 1
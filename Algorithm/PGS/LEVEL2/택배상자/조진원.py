from collections import deque

def solution(order):
    sub = []
    main = []
    container = deque([x for x in range(1,len(order)+1)])
    
    while True :
        c = ''
        for box in order :

            # 서브 컨테이너 마지막과 일치하면 꺼내기
            if len(sub) > 0 and sub[-1] == box :
                main.append(sub.pop())

            # 컨테이너 첫번째와 일치하면 꺼내기
            elif len(container) > 0 and container[0] == box :
                main.append(container.popleft())
            
            # 주 컨테이너쪽에 있는 것을 꺼내야 한다면
            elif len(container) > 0 and box > container[0] :

                # 그것이 나올떄 까지 서브컨테이너로 옮기기
                while box != container[0] :
                    sub.append(container.popleft())
                main.append(container.popleft())
            
            # 그 외의 경우는 더이상 옮길 수 없음
            else :
                c = 'pass'
                break
        
        if c == 'pass' :
            break
    
    return len(main)
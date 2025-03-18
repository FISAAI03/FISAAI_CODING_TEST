def solution(dirs):
    direction = {'U' : (0,1),
                 'D' : (0,-1),
                 'R' : (1,0),
                 'L' : (-1,0)}
    
    # 방문기록
    visited = set()
    
    x, y = 0, 0
    for move in dirs :
        # 좌표 이동
        dx, dy = x + direction[move][0], y + direction[move][1]
        
        
        # 범위 안에 있으면 저장
        if -5 <= dx <= 5 and -5 <= dy <= 5 :
            # 방문기록 저장, (출발, 도착) (도착, 출발) 형식으로 저장해서 그 경로를 기록
            visited.add((x,y,dx,dy))
            visited.add((dx,dy,x,y))
            
            # 이동
            x, y = dx, dy
        
        
    return len(visited) // 2
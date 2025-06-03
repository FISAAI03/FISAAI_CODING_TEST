def solution(schedules, timelogs, startday):
    answer = 0
    
    for schedule, timelog in zip(schedules, timelogs):
        # 희망 출근 시각 + 10분 계산
        hour, minute = divmod(schedule, 100)
        total_minute = hour * 60 + minute + 10
        maxtime = (total_minute // 60) * 100 + (total_minute % 60)
        
        chk = True
        for idx, time in enumerate(timelog):
            # 현재 요일 계산
            day = (startday + idx - 1) % 7 + 1
            if day in [6, 7]:  # 토요일, 일요일
                continue
            
            if time > maxtime:
                chk = False
                break
        
        if chk:
            answer += 1
    
    return answer

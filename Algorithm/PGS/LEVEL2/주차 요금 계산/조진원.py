import math

# 비용계산 함수
def cost(time, base_t, base_c, minute, fee) :
    if time <= base_t :
        return base_c
    else :
        total = base_c + math.ceil((time - base_t) / minute) * fee
        return total

def solution(fees, records):
    
    # 누적주차시간
    time_record = dict()
    # 입출상황
    in_out_record = dict()
    
    # 기록 정리
    for record in records :
        time, number, status = record.split()
        
        # time 정리
        h, m = time.split(":")
        total = int(h) * 60 + int(m)
        
        if status == 'IN' :
            if record not in in_out_record :
                in_out_record[number] = total
            else :
                pass
        elif status == 'OUT' :
            term = total - in_out_record[number]
            del in_out_record[number]
            # 기록
            if number not in time_record :
                time_record[number] = term
            else :
                time_record[number] += term
    
    
    # IN 기록만 있는 것들 처리
    if in_out_record :
        for number in in_out_record :
            term = (23*60 + 59) - in_out_record[number]
            
            # 기록
            if number not in time_record :
                time_record[number] = term
            else :
                time_record[number] += term
    
    
    answer = []
    # 요금정보
    base_t, base_c, minute, fee = fees
    
    # 정산하기
    for number in sorted(time_record) :
        charge = cost(time_record[number], base_t, base_c, minute, fee)
        answer.append(charge)
        
    return answer
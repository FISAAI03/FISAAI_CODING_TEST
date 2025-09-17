def solution(book_time):
    # 예약 시간을 시작 시각 기준으로 정렬
    book_time = sorted(book_time, key=lambda x: x[0])
    
    # 방 번호를 key로 하고, 각 방의 예약 시간을 리스트로 저장
    rooms = dict()

    # 각 예약 정보를 순회
    for times in book_time:
        start, end = times

        # 문자열 시간을 분 단위로 변환 (HH:MM → minutes)
        start = int(start.split(":")[0]) * 60 + int(start.split(":")[1])
        end = int(end.split(":")[0]) * 60 + int(end.split(":")[1])

        # 기본적으로 새 방 번호는 현재 방 개수 + 1
        room_number = len(rooms) + 1

        # 방이 하나도 없으면 첫 방을 만들어 예약 추가
        if len(rooms) == 0:
            rooms[room_number] = [(start, end)]
        
        else:
            # 현재 예약을 기존 방에 넣을 수 있는지 판단하는 플래그
            is_newroom = True

            # 모든 기존 방을 확인
            for room in rooms:
                # 해당 방의 마지막 예약 종료 시간 확인
                r_start, r_end = rooms[room][-1]

                # 청소 시간(10분)을 고려했을 때 현재 예약이 이 방에 들어갈 수 있다면
                if r_end + 10 <= start:
                    rooms[room].append((start, end))  # 예약 추가
                    is_newroom = False  # 새 방 필요 없음
                    break  # 조건 만족했으므로 반복 종료

            # 모든 방에 넣지 못했으면 새 방 생성
            if is_newroom:
                rooms[room_number] = [(start, end)]
    
    # 사용된 방의 수 반환
    return len(rooms)

###


def solution(book_time):
    # 총 24시간 * 60분 = 1440분 (00:00 ~ 23:59)
    # 분 단위로 시간을 관리하기 위해 1440분 길이의 배열을 생성합니다.
    # 퇴실 후 10분간의 청소 시간을 고려하여 넉넉하게 1440 + 10 = 1450분까지 인덱스를 사용합니다.
    timeline = [0] * (24 * 60 + 11)  # 24시간 * 60분 = 1440분. 0부터 1439까지의 인덱스. +10분 여유를 위해 11을 더함 (최대 1450분까지 커버)

    # 예약된 시간들을 순회합니다.
    for start_str, end_str in book_time:
        # 입실 시간을 분 단위로 변환합니다. (예: "15:00" -> 15 * 60 + 0 = 900)
        start = int(start_str[:2]) * 60 + int(start_str[3:])
        # 퇴실 시간을 분 단위로 변환하고, 청소 시간 10분을 더합니다.
        # 이 시간은 해당 객실을 더 이상 사용하지 않게 되는 시간입니다.
        end = int(end_str[:2]) * 60 + int(end_str[3:]) + 10  # 청소시간 10분 포함

        # 해당 시간에 방을 사용하는 손님이 들어오므로 필요한 방의 개수를 1 증가시킵니다.
        timeline[start] += 1  # 입실 시점에 방 사용 개수 +1
        # 청소 시간을 포함한 퇴실 시점에 방 사용이 끝나므로 필요한 방의 개수를 1 감소시킵니다.
        timeline[end] -= 1    # 청소 후 퇴실 시점에 방 사용 개수 -1

    max_rooms = 0  # 필요한 최대 방의 개수를 저장할 변수 초기화
    current = 0    # 현재 시점에 사용 중인 방의 개수를 저장할 변수 초기화

    # 타임라인 배열을 순회하면서 각 시점(분)에 필요한 방의 개수를 계산합니다.
    for t in timeline:
        current += t  # 이전 시점까지의 방 개수에 현재 시점의 변화량(입실 또는 퇴실)을 더합니다.
        # 현재까지 계산된 방 개수(current)와 이전에 기록된 최대 방 개수(max_rooms)를 비교하여
        # 더 큰 값을 max_rooms에 저장합니다.
        max_rooms = max(max_rooms, current)

    # 모든 시간을 고려했을 때 동시에 가장 많이 필요했던 방의 개수를 반환합니다.
    return max_rooms
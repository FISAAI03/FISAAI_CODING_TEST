def solution(players, m, k):
    server_expiry = [0 for _ in range(24)]  # 각 시간대에 만료될 서버 수를 기록하는 배열

    answer = 0  # 총 서버 증설 횟수
    n = 0       # 현재 운영 중인 서버 수

    for hour, player in enumerate(players):
        # 현재 시각에 만료되는 서버 수를 반영하여 현재 운영 중인 서버 수 업데이트
        n += server_expiry[hour]

        # 현재 운영 중인 서버 수(n)로 감당할 수 있는 최대 이용자 수는 (n * m)
        # 현재 이용자 수가 (n+1)*m 이상이면 서버를 증설해야 함
        if player >= ((n + 1) * m):
            # 추가로 필요한 서버 수 계산
            add = (player - m * n) // m
            n += add           # 현재 서버 수에 추가
            answer += add      # 증설 횟수 누적

            # 새로 증설한 서버들은 k시간 뒤에 만료되므로, 해당 시각에 반영
            # 예: hour=3, k=5 → server_expiry[8]에 -add 기록
            if hour + k < 24:
                server_expiry[hour + k] = -add  # k시간 후에 해당 서버 수만큼 만료 처리

    return answer  # 최소 서버 증설 횟수 반환
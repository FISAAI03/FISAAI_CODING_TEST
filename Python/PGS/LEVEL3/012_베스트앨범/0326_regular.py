import heapq

def solution(genres, plays):
    answer = []

    genres_dict = {}
    for i in range(len(genres)):
        if not genres[i] in genres_dict:
            genres_dict[genres[i]] = [(-plays[i], i)]
        else:
            genres_dict[genres[i]].append((-plays[i], i))

    ## 인기순 나열
    orders = []
    for k, v in genres_dict.items():
        v_sum = 0
        for play, _ in v:
            v_sum += play
        orders.append((k, v_sum))
    orders.sort(key=lambda x:x[1])

    ## 곡 선정
    for genre, _ in orders:
        heap = []
        for play in genres_dict[genre]:
            heapq.heappush(heap, play)

        count = 0
        while heap:
            if count < 2:
                answer.append(heapq.heappop(heap)[1])
                count += 1
            else:
                break

    return answer
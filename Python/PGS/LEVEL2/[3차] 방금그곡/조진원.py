def solution(m, musicinfos):
    # 1. 기억한 멜로디 m에서 샵(#)이 붙은 음을 한 글자로 치환
    #    C# -> V, D# -> W, F# -> X, G# -> Y, A# -> Z, B# -> K
    #    이렇게 해야 'C'와 'C#'처럼 겹치는 음을 구분 가능
    m = m.replace("C#", "V").replace("D#", "W").replace("F#", "X")\
         .replace("G#", "Y").replace("A#", "Z").replace("B#", "K")
    
    # 2. 조건을 만족하는 후보 곡을 담을 리스트 초기화
    answer = []
    
    # 3. musicinfos 배열을 순회하며 각 곡 처리
    for i, musicinfo in enumerate(musicinfos):
        # 곡 정보 분리: 시작 시간, 종료 시간, 곡 제목, 악보
        st, et, name, music = musicinfo.split(",")
        
        # 악보에서도 샵(#)이 붙은 음을 동일하게 치환
        music = music.replace("C#", "V").replace("D#", "W").replace("F#", "X")\
                     .replace("G#", "Y").replace("A#", "Z").replace("B#", "K")
        
        # 시작 시간과 종료 시간을 분 단위로 변환
        sh, sm = map(int, st.split(":"))
        eh, em = map(int, et.split(":"))
        time = (eh*60 + em) - (sh*60 + sm)  # 총 재생 시간(분)
        
        # 재생 시간에 맞춰 실제 들리는 멜로디 생성
        # 음악이 재생 시간보다 짧으면 반복 재생
        melody = music * (time // len(music)) + music[:time % len(music)]
        
        # 기억한 멜로디가 실제 재생 멜로디 안에 포함되는지 확인
        if m in melody:
            # 포함되면 후보곡 리스트에 (곡 제목, 재생 시간, 입력 순서) 추가
            answer.append((name, time, i))
    
    # 후보곡이 없으면 "(None)" 반환
    if not answer:
        return "(None)"
    
    # 후보곡이 여러 개면
    # 1순위: 재생 시간 길이 내림차순
    # 2순위: 입력 순서 오름차순
    # 정렬 후 첫 번째 곡 제목 반환
    return sorted(answer, key=lambda x: (-x[1], x[2]))[0][0]

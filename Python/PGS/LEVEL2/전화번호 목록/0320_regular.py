def solution(phone_book):
    answer = True

    s_phone_book = sorted(phone_book)
    for i in range(len(s_phone_book) - 1):
        if s_phone_book[i] == s_phone_book[i + 1][:len(s_phone_book[i])]:
            answer = False
    return answer
def solution(num) :
    num = list(str(num))

    return int(''.join(sorted(num, reverse=True))) - int(''.join(sorted(num)))

print(solution(5924))
print(solution(3904))
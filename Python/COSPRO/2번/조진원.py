def solution(money, cost, name) :
    max = 0
    answer = ''

    for n, [k, v] in zip(name, cost) :
        lens = money // v * k
        if lens > max :
            answer = n
            max = lens

    return answer
    



money = 100,000
cost = [[50, 5000], [20, 1000], [20, 5000], [50, 1000]]
name = ["A", "B", "C", "D"]

print(solution(money, cost, name))
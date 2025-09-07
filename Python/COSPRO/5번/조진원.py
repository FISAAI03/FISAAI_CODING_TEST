from collections import Counter

def solution(menu, votes) :
    count = sorted(Counter(votes).items(), key = lambda x : -x[1])
    return [count[0][0], count[1][0]]



menu1 = ["Latte", "Americano","Espresso"]
votes1 = ["Latte", "Americano", "Espresso", "Latte", "Americano", "Americano", "Latte", "Americano", "Americano", "Latte", "Latte", "Latte"]

menu2 = ["MochaLatte", "GreenTea", "Cappuccino"]
votes2 = ["GreenTea", "GreenTea", "MochaLatte", "GreenTea", "Cappuccino", "Cappuccino"] 


print(solution(menu1,votes1))
print(solution(menu2,votes2))
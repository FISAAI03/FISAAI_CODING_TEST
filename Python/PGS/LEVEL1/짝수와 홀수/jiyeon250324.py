#sol 1
def solution(num):
    if num % 2 == 0:
        return "Even"
    else :
        return "Odd"


#sol 2
def evenOrOdd(num):
    if num%2:
        return "Odd"

    return "Even"


#sol 3
def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]
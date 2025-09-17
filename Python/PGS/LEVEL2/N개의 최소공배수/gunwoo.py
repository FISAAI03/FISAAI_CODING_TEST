def solution(arr):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    lcm = arr[0]
    for num in arr[1:]:
        lcm = lcm * num // gcd(lcm, num)
    
    return lcm

def prime(num):
    i = 5
    while i < int(num**(1/2))+1:
        if num % i == 0:
            return False
        i += 2

    return True

m, n = map(int, input().split())

for i in range(m, n+1):
    if (i == 2) or (i == 3):
        print(i)
    elif (i == 1) or (i % 2 == 0) or (i % 3 == 0):
        pass
    elif prime(i):
        print(i)

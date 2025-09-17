# 최대값을 만든다 = 가장 큰 두 수를 선택해서, 곱한다.
def solution(numbers):
    max_num = sorted(numbers)[::-1]
    return max_num[0] * max_num[1]

"""
sorted(list), or list.sort() 둘다 가능
다른 풀이.
```
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]

```
def solution(numbers):
    num1 = 0
    num2 = 0
    answer = 0

    numbers.sort()

    num1 = numbers.pop()
    num2 = numbers.pop()
    answer = num1 * num2

    return answer
```
"""
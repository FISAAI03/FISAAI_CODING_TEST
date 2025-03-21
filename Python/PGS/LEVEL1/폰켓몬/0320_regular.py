def solution(nums):
    answer = 0
    max_num = len(nums) / 2
    bag = []

    for num in nums:
        if not num in bag:
            bag.append(num)
        if len(bag) == max_num:
            break
    answer = len(bag)

    return answer
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3))
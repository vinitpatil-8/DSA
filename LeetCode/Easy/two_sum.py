nums = [2,7,11,15]
target = int(input())
for i, x in enumerate(nums):
    for a, b in enumerate(nums):
        if i != a and (x + b) == target:
            print([i, a])
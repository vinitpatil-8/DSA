nums = [2,7,11,15]
target = int(input())
seen = {}  # key: number, value: index

for index, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        print([seen[complement], index])
    seen[num] = index
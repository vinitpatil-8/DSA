# Move Zeros to the end
# Brute Force

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

temp = []
for i in range(len(arr)):
    if arr[i]!=0:
        temp.append(arr[i])
for i in range(len(temp)):
    arr[i] = temp[i]
for i in range(len(temp), len(arr)):
    arr[i] = 0

print(arr)

# Optimal
nums = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]


j = -1
for i in range(len(nums)):
    if nums[i] == 0:
        j = i
        break
for i in range(j+1, len(nums)):
    if j==-1:
        break
    if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1

print(nums)
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


# Union Of Two Sorted Array

print("Union of Two Sorted Array")
arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]

# Brute Force way

set1 = set(arr1)
set2 = set(arr2)
result = set1 | set2
print(result)

# Optimal
print("Optimal Approach")
arr3 = [1, 1, 2, 3, 4, 5]
arr4 = [2, 3, 4, 4, 5, 6]

n3 = len(arr3)
n4 = len(arr4)
i = 0
j = 0
union = []
while i<n3 and j<n4:
    if arr3[i] <= arr4[j]:
        if len(union) == 0 or union[-1] != arr3[i]:
            union.append(arr3[i])
        i += 1
    else:
        if len(union) == 0 or union[-1] != arr4[j]:
            union.append(arr4[j])
        j += 1
if i!=n3:
    while i<n3:
        if len(union) == 0 or union[-1] != arr3[i]:
            union.append(arr3[i])
        i += 1
if j!=n4:
    while j<n4:
        if len(union) == 0 or union[-1] != arr4[j]:
            union.append(arr4[j])
        j += 1
print(union)


# Intersection of Two Arrays
print("Intersection of Two Arrays")

nums1 = [1, 2, 2, 3, 3, 4, 5, 6]
nums2 = [2, 3, 3, 5, 6, 6, 7]

i = 0
j = 0
n1 = len(nums1)
n2 = len(nums2)
intersection = []
while i<n1 and j<n2:
    if nums1[i] < nums2[j]:
        i += 1
    elif nums1[i] > nums2[j]:
        j += 1
    else:
        if len(intersection) == 0 or intersection[-1] != nums1[i]:
            intersection.append(nums1[i])
        i += 1
print(intersection)    
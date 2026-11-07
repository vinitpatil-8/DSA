# Left Rotate an Array - 
# by 1 place
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)

temp = arr[0]
for i in range(1, n):
    arr[i-1] = arr[i]
arr[n-1] = temp
print(arr)


# by d places

arr2 = [1, 2, 3, 4, 5, 6, 7]
d = 10
# 8 rotations = 1 rotation because array size is 7
# Therefore, d = d % n

# solving - 

temp = []
n = len(arr2)
rotations = d%n

# Taking the elements we need to rotate
for i in range(rotations):
    temp.append(arr2[i])

# Rotate Remaining Elements
for i in range(rotations, n):
    arr2[i-rotations] = arr2[i]

# Add the elements we need to Rotate
for i in range(n-rotations, n):
    arr2[i] = temp[i-(n-rotations)]

print(arr2)

# TC - O(n + d)
# SC - O()
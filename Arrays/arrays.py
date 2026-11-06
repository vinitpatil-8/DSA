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
# 8 rotations = 1 rotation because array size is 7
# Therefore, d = d % n
d = 3
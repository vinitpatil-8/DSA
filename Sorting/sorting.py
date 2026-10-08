# 1. Selection sort
# O(n²)
print("1. Selection sort")
arr = [13, 46, 24, 52, 20, 9]
n = len(arr)
for i in range(0, n-1): # should be (n-2) but python doesnt take last digit thats why did +1
    mini = i
    for j in range(i, n): # should be (n-1) but python doesnt take last digit thats why did +1
        if arr[j] < arr[mini]:
            mini = j
    arr[mini], arr[i] = arr[i], arr[mini]

print(arr)



# 2. Bubble sort
# avg and worst case - O(n²)
# best case - O(n)
arr2 = [13, 46, 24, 52, 20, 9]
n2 = len(arr2)
print("2. Bubble sort")
for i in range(n2-1, 0, -1):
    swap = 0
    for a in range(0, i):
        if arr2[a]>arr2[a+1]:
            arr2[a], arr2[a+1] = arr2[a+1], arr2[a]
            swap = 1
    if swap!=1:
        break
print(arr2)

# 3. Insertion sort
arr3 = [13, 46, 24, 52, 20, 9]
n3 = len(arr3)
print("3. Insertion sort")
for i in range(1, n3):
    j=i
    while j>0 and arr3[j-1] > arr3[j]:
        arr3[j-1], arr3[j] = arr3[j], arr3[j-1]
        j= j-1
print(arr3)
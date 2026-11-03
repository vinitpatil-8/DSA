nums = [4, 6, 2, 5, 7, 9, 3, 5, 7, 9, 1, 2, 3, 5, 2, 1, 7, 9, 10, 142, 434, 35454, 354, 1, 2, 10]


def f(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i<j:
        while arr[i]<=pivot and i<high:
            i += 1
        while arr[j]>pivot and j>low:
            j -= 1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quickSort(arr, low, high):
    if low<high:
        partition = f(arr, low, high)
        quickSort(arr, low, partition-1)
        quickSort(arr, partition+1, high)

quickSort(nums, 0, len(nums)-1)
print(nums)
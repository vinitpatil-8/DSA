nums = [2, 6, 9, 2, 2, 6, 9, 4]

# merge function
def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1

    # two pointer
    while left<=mid and right<=high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left = left + 1
        else:
            temp.append(arr[right])
            right = right + 1

    # right side got exhausted
    while left<=mid:
        temp.append(arr[left])
        left = left + 1

    # left side got exhausted
    while right<=high:
        temp.append(arr[right])
        right = right + 1

    # merge the temp array into main array
    for i in range(low, high+1):
        arr[i] = temp[i-low]


# divide function
def mergeSort(arr, low, high):
    # stop when hypothetical array contains only 1 element
    if low>=high:
        return
    mid = (low+high) // 2
    # first recursion
    mergeSort(arr, low, mid)
    # second recursion
    mergeSort(arr, mid+1, high)
    # merging into main array
    merge(arr, low, mid, high)

mergeSort(nums, 0, 7)

print(nums)
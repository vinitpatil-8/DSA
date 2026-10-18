#### Date - 17/10/2026

# Sorting -

[Reference File](merge_sort.py)

## Merge sort Pseudocode - 

```
merge(arr, low, mid, high){
    temp = []
    left = low
    right = mid+1

    # two pointer
    while(left<=mid and right<=high){
        if (arr[left] <= arr[right]){
            temp.append(arr[left])
            left = left + 1
        }
        else{
            temp.append(arr[right])
            right = right + 1
        }
    }

    # right side got exhausted
    while(left<=mid){
        temp.append(arr[left])
        left = left + 1
    }

    # left side got exhausted
    while(right<=high){
        temp.append(arr[right])
        right = right + 1
    }

    # merge the temp array into main array
    for (i = low, i < high+1, i++){
        arr[i] = temp[i-low]
    }
}




mergeSort(arr, low, high){
    
    if(low >= high){
        return
    }

    mid = (low+high) / 2

    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)

    merge(arr, low, mid, high)
}

```

### Time complexity - O(N log N)
### Space complexity - O(N) 

### Questions solved - 
1. 912 Sort an array - [File](/LeetCode/Medium/sort_an_array.py)
2. 88 Merge Sorted array - [File](/LeetCode/Easy/merge_sorted_array.py)
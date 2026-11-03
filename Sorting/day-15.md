#### Date - 20/10/2026

# Quick sort -

Steps <br>

1. Pick a pivot (ex. first element of array)
2. Keep 2 pointers (At start of array and end) {low&high and i&j}
3. Compare with pivot and swap (smaller on left and bigger on right)
4. Keep repeating till i crosses j
5. Once done, swap pivot with last small element
6. Perform quicksort (recursion) on two array (low,pivot-1) and (pivot+1,high) 

[Reference File](quicksort.py)

## Quick sort Pseudocode - 

```
f(arr, low, high){
    pivot = arr[low]
    i = low
    j = high
    while(i<j){
        while(arr[i]<pivot && i<=high){
            i++
        }
        while(arr[j]>pivot && j>=low){
            j--
        }
        if(i<j){
            swap(arr[i], arr[j])
        }
    }
    swap(arr[low], arr[j])
    return j
}

qs(arr, low, high){
    if(low<high){
        partition = f(arr,low,high)
        qs(arr, low, partition-1)
        qs(arr, partition+1, high)
    }
}
```

### Time complexity - O(N log N)
### Space complexity - O(1) 
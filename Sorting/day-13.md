#### Date - 08/10/2026

# Sorting -

[Reference File](sorting.py)

1. **Selection sort -** 
<br><br>
    Select Minimums and swap their positions <br>
    *Outer loop* - Goes from 0 to n-2 (n-1 in python) <br>
    *Inner loop* - Goes from 0 to n-1 (n in python) <br>
    - best, worst, avg case - O(n²) <br>

2. **Bubble sort -**
<br><br>
    Pushes the max to last by **Adjacent swaps** <br>
    *Outer loop* - Goes from n-1 to 0 <br>
    *Inner loop* - Goes from 0 to i-1 (i is outer loop iteration, i in python) <br>
    - avg and worst case - O(n²) <br>
    - best case - O(n) <br>

3. **Insertion sort -**
<br><br>
    Takes an element and places it in its correct place <br>
    Starts from 1-sized array and keeps expanding <br>
    Shifts elements to left (if needed) <br><br>
    *Outer loop* - Goes from 0 to n-1 (n in python) <br>
    *Inner loop (while loop)* - Goes till **j>0 and arr[j-1]>arr[j]** (j=1) (j--)
    - worst, avg case - O(n²) <br>
    - best case - O(n) --- *While loop doesnt run*

4. **Merge sort -**
<br><br>
    Divide and Conquer algorithm that recursively splits the array in half, sorts each half, and merges them.
    
    Divide - Split array at mid = (low + high) // 2 until single elements remain

    Conquer - Merge two sorted halves back together using two pointers

    - Worst, avg, and best case - **O(n \log n)**
    
    - Space complexity - **O(n)** (requires extra space for merging)
    - Stable sorting algorithm
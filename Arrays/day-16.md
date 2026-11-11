#### Date - 03/11/2026

[Reference File](arrays.py)

# Linear Search (Pseudocode) - 

```
nums = [1, 4, 5, 6, 8, 9]
target = 6

for index, item in enumerate(nums):
    if item==target:
        return index

return -1
```

# Second Largest Element in an Array - 

```
nums = [1, 4, 5, 6, 8, 9]
largest = 0
slargest = -1

for i in nums:
    if i>largest:
        largest = i
for i in nums:
    if i>slargest and i<largest:
        slargest = i

return slargest

```
Problem solved - [File](/LeetCode/Easy/second_largest_digit_in_string.py)

# Maximum Consecutive Ones -

Problem solved - [File](/LeetCode/Easy/max_consecutive_ones.py)

# Left Rotate an Array - 

1. By 1 place 
2. By D places 
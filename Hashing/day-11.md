#### Date - 26/09/2026

# Hashing -
<br>
Precomputing a array with a dictionary(hash table) to reduce time complexity
<br>
<br>

*There are two ways in python to do this* -
<br>

1. **Collections**
2. **dict.get()**

Take a look at [Hashing](hashing.py) 

<br>
<br>

## Hashing Characters :-

We do it using ASCII Values

![ASCII Values](/Assets/ascii.png)

<br>

**In python we use ord() to convert char to ASCII**
<br>

**In python we use chr() to convert ASCII to char**
<br>

Take a look at [Hashing Characters](char_hashing.py) 


Also take a look at [Leetcode Problem - Contains Duplicate](/LeetCode/Easy/contains_duplicate.py)

## Why use Dict or set instead of lists ?
<br>

**list** ***(O(n) search)***: Scans item-by-item from start to finish. Inside a loop, this causes *O(n²)* time (Time Limit Exceeded).

**Set / dict** ***(O(1) search)***: Uses a mathematical hash function to jump directly to the memory location. Inside a loop, this runs in O(n) optimal time.
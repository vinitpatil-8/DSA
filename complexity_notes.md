# ⏱️ Time & Space Complexity — Quick Notes

## Time Complexity

Time complexity describes how the number of operations grows as the input size increases.

We use **Big-O notation** to represent it.

### Big-O Rules

1. **Always consider the worst case**
   - Best Case → Least operations
   - Average Case → Average operations
   - Worst Case → Most operations
   - For normal analysis, use the worst case.

2. **Ignore constants**
   - `O(3n)` → `O(n)`
   - `O(5n²)` → `O(n²)`
   - `O(100n)` → `O(n)`

3. **Ignore lower-order terms**
   - `O(n² + n)` → `O(n²)`
   - `O(n³ + n² + n)` → `O(n³)`
   - `O(n + log n)` → `O(n)`
   - `O(n² + 100)` → `O(n²)`

---


# 💾 Space Complexity

Space complexity describes how much memory an algorithm uses as input size increases.

### Space Complexity

`Input Space + Auxiliary Space`

### Input Space

Memory required to store the input.

### Auxiliary Space

Extra memory used by the algorithm to solve the problem.

### O(1) Space

```python
a = 10
b = 20
c = a + b
```

Fixed amount of extra memory.

**Space:** `O(1)`

### O(n) Space

```python
arr = [0] * n
```

Memory grows with `n`.

**Space:** `O(n)`

---

# 📊 Complexity Cheat Sheet

| Complexity | Name | Example |
|---|---|---|
| `O(1)` | Constant | Array access |
| `O(log n)` | Logarithmic | Binary Search |
| `O(n)` | Linear | Single loop |
| `O(n log n)` | Linearithmic | Merge Sort |
| `O(n²)` | Quadratic | Nested loops |
| `O(n³)` | Cubic | 3 nested loops |
| `O(2ⁿ)` | Exponential | Some recursive solutions |
| `O(n!)` | Factorial | Permutations |

---

# 🧠 Quick Method to Find Complexity

### Step 1
Count how many times the code runs.

### Step 2
For nested loops, multiply iterations.

`n × n = n²`

### Step 3
For separate blocks, add complexities.

`O(n) + O(n²)`

### Step 4
Ignore constants.

`O(3n²) → O(n²)`

### Step 5
Ignore lower-order terms.

`O(n² + n) → O(n²)`

### Final Format

```text
Time Complexity: O(...)
Space Complexity: O(...)
```

---

# ⚡ Golden Rules

- **Worst Case**
- **Ignore Constants**
- **Ignore Lower-Order Terms**

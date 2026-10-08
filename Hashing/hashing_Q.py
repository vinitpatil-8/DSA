# Longest Consecutive Sequence
print("Longest Consecutive Sequence")
print("Brute force")

arr = [102, 4, 100, 1, 101, 3, 2, 1, 1, 4]

longest = 1
for i in arr:
    find = i + 1
    for j in arr:
        
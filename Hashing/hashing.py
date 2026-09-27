from collections import Counter
# two ways of doing this
# 1. Collections
# 2. dict with .get()


# Check the frequencies of numbers occuring in array
# dict with .get()
print("Check the frequencies of numbers occuring in array")
size = int(input("Enter size of array :"))
arr = []
for i in range(0, size):
    arr.append(int(input()))
print(f"{arr} : This is the array")

# precomputation 
hash = {} # key: number value: occurence
for i in arr:
    # .get(i, 0) returns the current count, or 0 if 'i' isn't in hash_map yet
    hash[i] = hash.get(i, 0) + 1

queries = int(input("Enter number of queries :"))
for _ in range(queries):
    number = int(input())
    # Safely fetch count, printing 0 if 'number' never appeared in the array
    print(f"{number} appeared {hash.get(number, 0)} times in array")

# Collections

# Precomputation in 1 line
hash_map = Counter(arr)

# Queries
queries = int(input())
for _ in range(queries):
    number = int(input())
    print(hash_map[number])  # Returns 0 for missing elements
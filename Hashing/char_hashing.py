# ascii_value = ord("b") - ord("a")
# Detect occurence of alphabets
# Both lowercase and uppercase

# lowercase & uppercase by dict.get()
s = input("Input a string: ")
queries = int(input("Enter no. of queries: "))
hash_map = {}
for i in s:
    hash_map[ord(i)] = hash_map.get(ord(i), 0) + 1

for i in range(queries):
    char = input()
    ascii_char = ord(char)
    print(hash_map.get(ascii_char, 0))

# by collections
from collections import Counter
hashes = Counter(s)
for i in range(queries):
    char = input()
    print(hashes[char])
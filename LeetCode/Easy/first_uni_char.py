# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         hash_map = {}
#         for i in s:
#             hash_map[i] = hash_map.get(i, 0) + 1
#         for index, char in enumerate(s):
#             if hash_map[char] == 1:
#                 return index
#         return -1
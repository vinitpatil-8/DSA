# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         hash_map = {}
#         for item in strs:
#             tup = [0] * 26
#             for i in item:
#                 tup[int(ord(i))-int(ord('a'))] += 1
#             key = tuple(tup)
#             hash_map.setdefault(key, []).append(item)


#         output = list(hash_map.values())
#         return output

# Initial Solution
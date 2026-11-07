# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         words = s.split()
#         if len(pattern) != len(words):
#             return False
#         hash_map_p = {}
#         hash_map_s = {}
#         for i in range(len(pattern)):
#             if pattern[i] not in hash_map_p and words[i] not in hash_map_s:
#                 hash_map_p[pattern[i]] = words[i]
#                 hash_map_s[words[i]] = pattern[i]
#             else:
#                 if pattern[i] in hash_map_p:
#                     if hash_map_p[pattern[i]] != words[i]:
#                         return False
#                 if words[i] in hash_map_s:
#                     if hash_map_s[words[i]] != pattern[i]:
#                         return False
#         return True


# Optimal Solution

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        return len(pattern) == len(words) and len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))
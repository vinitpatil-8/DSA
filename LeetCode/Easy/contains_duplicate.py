# Hashing Approach


# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         hash_map = set()
#         for i in nums:
#             if i in hash_map:
#                 return True
#             hash_map.add(i)
#         return False

# Optimal and set Approach

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         nums_set = set(nums)
#         if len(nums_set) == len(nums):
#             return False
#         else: return True

# As set only contains UNIQUE values
# Hash map approach

# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         hash_map = {}
#         for i in range(len(nums)):
#             if nums[i] not in hash_map:
#                 hash_map.setdefault(nums[i], nums[i])
#         nums[:] = list(hash_map.values())
#         return len(nums)

# Two pointer Approach

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = 0
        counter = 1
        for index, element in enumerate(nums):
            if nums[unique] != element:
                unique += 1
                nums[unique], nums[index] = nums[index], nums[unique]
                counter += 1
        return counter
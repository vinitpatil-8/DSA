# class Solution:
#     def numIdenticalPairs(self, nums: list[int]) -> int:
#         counts = {}
#         total_pairs = 0

#         for num in nums:
#             total_pairs += counts.get(num, 0)

#             counts[num] = counts.get(num, 0) + 1

#         return total_pairs
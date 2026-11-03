# class Solution:
#     def minMoves(self, nums: List[int]) -> int:
#         biggest = max(nums)
#         total = 0
#         for i in nums:
#             total += biggest-i
#         return total
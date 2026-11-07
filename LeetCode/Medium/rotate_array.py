# First Approach

# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         n= len(nums)
#         k=k%n
#         def reverse(a, b):
#             for i in range(((b-a+1)//2)):
#                 nums[a+i], nums[b-i] = nums[b-i], nums[a+i]
#         reverse(0, n-k-1)
#         reverse(n-k, n-1)
#         reverse(0, n-1)
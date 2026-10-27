class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for index, item in enumerate(nums):
            if item>=target:
                return index
        return len(nums)
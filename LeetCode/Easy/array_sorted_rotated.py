class Solution:
    def check(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        change = 0
        for i in range(len(nums)):
            if nums[i]<nums[i-1]:
                change += 1
            if change>1:
                return False
        return True
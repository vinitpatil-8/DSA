class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        dominant = 0
        if len(nums) == 1:
            return 1
        for i in range(len(nums)):
            if i>0 and i<len(nums)-1:
                if (nums[i-1]+nums[i+1])/2 <= nums[i]:
                    dominant += 1
            elif i==0:
                if nums[i+1] <= nums[i]:
                    dominant += 1
            else:
                if nums[i-1] <= nums[i]:
                    dominant += 1
        return dominant
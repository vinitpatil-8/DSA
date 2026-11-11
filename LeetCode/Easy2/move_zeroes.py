class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        for i in range(j+1, len(nums)):
            if j==-1:
                break
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        
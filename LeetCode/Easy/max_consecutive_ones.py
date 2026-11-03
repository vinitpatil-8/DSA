class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maximum = 0
        count = 0
        for i in nums:
            if i==1:
                if count>=maximum:
                    maximum += 1
                count += 1
            elif i==0:
                count = 0
        return maximum
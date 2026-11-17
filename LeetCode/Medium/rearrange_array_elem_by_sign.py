# Brute Force Approach
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = []
        neg = []
        output = []
        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)
        for i in range(len(nums)):
            if i%2==0:
                output.append(pos[i//2])
            else:
                output.append(neg[(i//2)])
        return output      

# Another Approach

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        flipper = True
        neg = 0
        pos = 0
        output = []
        while len(output) < len(nums):
            if flipper:
                while nums[pos] < 0:
                    pos += 1
                output.append(nums[pos])
                pos += 1
                flipper = False
            else:
                while nums[neg] > 0:
                    neg += 1
                output.append(nums[neg])
                neg += 1
                flipper = True
        return output     


# Optimal

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        output = [0] * len(nums)
        neg = 0
        pos = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                output[pos*2] = nums[i]
                pos += 1
            else:
                output[neg*2+1] = nums[i]
                neg += 1
        return output                   
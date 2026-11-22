class Solution:
    def minCost(self, nums: list[int]) -> int:
        n = len(nums)
        if all(x == nums[0] for x in nums):
            return 0
        lowCost = float('inf')
        k = 1
        for i in range(1, n-1):
            if i > 1 and nums[i] == nums[i-1]:
                k+=1
            else:
                k=1
            lowCost = min(lowCost, (n-k) * nums[i])
        i = 0
        j = n - 1
        while nums[i] == nums[0]:
            i += 1
        i -= 1
        if i>=1:
            lowCost = min(lowCost, (n-i-1)*nums[0])
        while nums[j] == nums[n-1]:
            j -= 1
        j += 1
        if j<=n-2:
            lowCost = min(lowCost, (j*nums[n-1]))
        return lowCost
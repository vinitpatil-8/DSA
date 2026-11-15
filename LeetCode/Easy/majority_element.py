# hash map approach
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
            if hashmap[nums[i]] > len(nums) // 2:
                return nums[i]


# simple method
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
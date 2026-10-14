class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        hash_map = {}
        n = len(nums)
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1
            if hash_map[i] > n/2:
                return i
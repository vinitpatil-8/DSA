class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        hash_map = {}
        for index, item in enumerate(nums):
            hash_map[item] = index
        for i in range(1, max(hash_map)+2):
            if i not in hash_map:
                return i
        i = 1
        while True:
            if i not in hash_map:
                return i
            i += 1
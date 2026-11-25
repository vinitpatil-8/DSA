class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        hash_map = {}
        output = []
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        for i in range(1, len(nums)+1):
            if i not in hash_map:
                output.append(i)
        return output
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         k = len(nums)
#         mod = []
#         for i in range(k):
#             if nums[i] == val:
#                 k = k - 1
#             else:
#                 mod.append(nums[i])
#         nums.clear()
#         nums.extend(mod)
#         return k

# Best working solution

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index = write_index + 1
        return write_index
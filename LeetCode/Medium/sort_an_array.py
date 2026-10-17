# class Solution:
#     def sortArray(self, nums: list[int]) -> list[int]:
#         def merge(arr, low, mid, high):
#             temp = []
#             left = low
#             right = mid+1
#             while left<=mid and right<=high:
#                 if arr[left] <= arr[right]:
#                     temp.append(arr[left])
#                     left = left + 1
#                 else:
#                     temp.append(arr[right])
#                     right = right + 1
#             if left<=mid:
#                 temp.extend(arr[left:mid+1])
#             elif right<=high:
#                 temp.extend(arr[right:high+1])
#             for i in range(low, high+1):
#                 arr[i] = temp[i-low]

#         def divide(arr, low, high):
#             if low>=high:
#                 return
#             mid = (low+high) // 2
#             divide(arr, low, mid)
#             divide(arr, mid+1, high)
#             merge(arr, low, mid, high)
#         divide(nums, 0, len(nums)-1)
#         return nums


# After Optimizing
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        temp = [0] * len(nums)
        def merge(arr, low, mid, high):
            left = low
            k = low
            right = mid+1
            while left<=mid and right<=high:
                if arr[left] <= arr[right]:
                    temp[k] = arr[left]
                    left = left + 1
                else:
                    temp[k] = arr[right]
                    right = right + 1
                k = k + 1
            if left<=mid:
                remaining_len = (mid + 1) - left
                temp[k : k + remaining_len] = arr[left : mid + 1]
            elif right<=high:
                remaining_len = (high + 1) - right
                temp[k:k+remaining_len] = arr[right:high+1]
            arr[low : high + 1] = temp[low : high + 1]

        def divide(arr, low, high):
            if low>=high:
                return
            mid = (low+high) // 2
            divide(arr, low, mid)
            divide(arr, mid+1, high)
            merge(arr, low, mid, high)
        divide(nums, 0, len(nums)-1)
        return nums
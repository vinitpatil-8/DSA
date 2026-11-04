# Initial Solution - 

# class Solution:
#     def distributeCandies(self, candyType: list[int]) -> int:
#         types = {}
#         for item in candyType:
#             types[item] = types.get(item, 0) + 1
#         keys = list(types.keys())
#         if (len(candyType)/2) >= len(keys):
#             return len(keys)
#         else:
#             return int(len(candyType)/2)

# Optimal Solution - 

# class Solution:
#     def distributeCandies(self, candyType: list[int]) -> int:
#         types = set(candyType)
#         if (len(candyType)/2) >= len(types):
#             return len(types)
#         else:
#             return int(len(candyType)/2)

# Shorter - 

class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        types = len(set(candyType))
        return min(len(candyType) // 2, types)
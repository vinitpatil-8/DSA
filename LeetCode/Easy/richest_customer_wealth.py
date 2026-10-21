# class Solution:
#     def maximumWealth(self, accounts: list[list[int]]) -> int:
#         scores = []
#         for i in range(len(accounts)):
#             score = 0
#             for j in range(len(accounts[i])):
#                 score += accounts[i][j]
#             scores.append(score)
#         return max(scores)

# MY solution

# Optimal Solution (Minimal too)

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(customer) for customer in accounts)
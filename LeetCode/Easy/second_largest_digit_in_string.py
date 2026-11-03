# class Solution:
#     def secondHighest(self, s: str) -> int:
#         only_digits = [int(char) for char in s if char.isdigit()]
#         largest = max(only_digits)
#         s_largest = -1
#         if not only_digits:
#             return -1
#         else:
#             for i in only_digits:
#                 if i>s_largest and i<largest:
#                     s_largest = i
#         return s_largest

# Optimal - 

class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        second_largest = -1
        for i in set(s):
            if i.isdigit():
                val = int(i)
                if val > largest:
                    second_largest = largest
                    largest = val
                elif val > second_largest and val < largest:
                    second_largest = val
                    
        return second_largest
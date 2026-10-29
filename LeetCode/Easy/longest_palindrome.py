class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = {}
        count = 0
        encountered = False
        for i in s:
            hash_map[i] = hash_map.get(i, 0) + 1
        for value in hash_map.values():
            if value%2==0:
                count += value
            else:
                count += value - 1
                encountered = True
        if encountered:
            return count+1
        else:
            return count
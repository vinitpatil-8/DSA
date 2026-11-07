class Solution:
    def countValidSubstrings(self, s: str) -> int:
        counter = 0
        l = 0

        for r in range(len(s)):
            if r >= 2 and s[r-2:r+1] == "abc":
                l = max(l, r-1)
            counter += (r - l+1)
        return counter
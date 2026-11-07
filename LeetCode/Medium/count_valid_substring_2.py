class Solution:
    def countValidSubstrings(self, s: str) -> int:
        counter = 0
        l = 0
        last_a = -1
        last_ab = -1

        for r in range(len(s)):
            if s[r] == 'a':
                last_a = r
            elif s[r] == 'b':
                if last_a != -1:
                    last_ab = last_a
            elif s[r] == 'c':
                if last_ab !=-1:
                    l=max(l, last_ab+1)
            counter += r-l+1
        return counter
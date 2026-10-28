class Solution:
    def validPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1

        while first<last:
            if s[first] == s[last]:
                first += 1
                last -= 1
            else:
                txt = s[first:last]
                txt2 = s[first+1:last+1]
                if txt[::-1] == txt or txt2[::-1] == txt2:
                    return True
                else:
                    return False
        return True
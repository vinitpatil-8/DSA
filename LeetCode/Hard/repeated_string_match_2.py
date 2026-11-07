import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str, x: int, y: int) -> bool:
        if y==0:
            return True
        substr = b*min(y,2)
        copies_needed = math.ceil(len(substr) / len(a)) + 1
        max_x = min(x, copies_needed+1)
        repeated_a = a*max_x
        i = repeated_a.find(substr)
        if i==-1:
            return False
        return (i+len(b)*y) <= (len(a)*x)
        if substr in str1:
            return True
        return False
s = 'badc'
t = 'baba'

hash_map = {}
hash_map_t = {}
def check(s, t):
    for i in range(len(s)):
        if s[i] not in hash_map and t[i] not in hash_map_t:
            hash_map[s[i]] = t[i]
            hash_map_t[t[i]] = s[i]
        elif s[i] in hash_map:
            if hash_map[s[i]] != t[i]:
                return False
        else:
            if hash_map_t[t[i]] != s[i]:
                return False
    return True

# Optimal - 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s))==len(set(t))==len(set(zip(s,t)))
        
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_map = {}
        for i in jewels:
            hash_map.setdefault(i, 0)
        score = 0
        for i in stones:
            if i in hash_map:
                score += 1
        return score
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = {}
        for i in ransomNote:
            hash_map[i] = hash_map.get(i, 0) + 1
        for j in magazine:
            if j in hash_map:
                hash_map[j] -= 1
        return all(value <= 0 for value in hash_map.values())
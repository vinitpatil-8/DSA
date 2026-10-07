class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maximus = []
        for i in sentences:
            words = i.split()
            maximus.append(len(words))
        return max(maximus)
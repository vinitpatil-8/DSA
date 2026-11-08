class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        output = []
        sub1 = []
        sub2 = []
        start = 0
        end = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                if start!=i:
                    temp = [s1[start:end+1], s2[start:end+1]]
                    output.append(temp)
                    start = i+1
                else:
                    start += 1
            else:
                end = i
                if i==len(s1)-1:
                    temp = [s1[start:end+1], s2[start:end+1]]
                    output.append(temp)
                    return output
        return output
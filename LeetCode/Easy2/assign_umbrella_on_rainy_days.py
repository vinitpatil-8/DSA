class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        alice = 0
        bob = 0
        output = []
        for i in range(len(rain)):
            if rain[i] == 1 and i<len(rain)-1:
                if rain[i+1] == 1 and alice<=bob:
                    alice += 1
                    output.append("Alice")
                else:
                    bob += 1
                    output.append("Bob")
            else:
                if rain[i] == 1:
                    output.append("Bob")
                else:
                    output.append("None")
        return output

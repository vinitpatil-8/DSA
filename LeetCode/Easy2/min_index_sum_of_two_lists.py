class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        commonStr = {}
        result = []
        min_index = float('inf')

        # map first list
        for index, item in enumerate(list1):
            commonStr[item] = index

        for index, item in enumerate(list2):
            if item in commonStr:
                current_index = commonStr.get(item) + index
                if current_index<min_index:
                    result = [item]
                    min_index = commonStr[item] + index
                elif current_index==min_index:
                    result.append(item)
                # early exit
                if min_index == 0:
                    return [item]
        return result
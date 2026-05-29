import copy
# Definition for a pair.
# class Pair:
def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return pairs
        ans = []
        ans.append(copy.deepcopy(pairs))
        for i in range(1, len(pairs)):
            while pairs[i].key < pairs[i-1].key:
                print(pairs[i-1].key, pairs[i].key)
                print(i, i-1)
                temp = pairs[i-1]
                pairs[i-1] = pairs[i]
                pairs[i] = temp
                if i-2 >= 0:
                    i -= 1
            ans.append(copy.deepcopy(pairs))
        return ans

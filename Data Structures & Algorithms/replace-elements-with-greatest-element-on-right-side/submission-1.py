class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_ = -1
            for j in range(i + 1, len(arr)):
                if arr[j] > max_:
                    max_ = arr[j]
            arr[i] = max_
        arr[-1] = -1
        return arr
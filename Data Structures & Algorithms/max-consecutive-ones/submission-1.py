class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        max_ = 0
        for i in nums:
            if i == 1:
                consec += 1
            elif i != 1 and consec > 0:
                if consec > max_:
                    max_ = consec
                consec = 0
        if consec > max_:
            max_ = consec
        return max_

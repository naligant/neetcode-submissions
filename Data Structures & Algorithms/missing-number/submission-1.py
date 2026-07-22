class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        unique = set()
        for i in nums:
            if i not in unique:
                unique.add(i)
        cnter = 0
        for num in unique:
            if cnter != num:
                break
            cnter += 1
        return cnter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = []

        for i in range(len(nums)):
            temp.append([nums[i],i])
        temp.sort()
        
        i = 0
        j = len(nums) - 1

        while i < j:
            cur = temp[i][0] + temp[j][0]
            if cur == target:
                return [min(temp[i][1], temp[j][1]), max(temp[i][1], temp[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []


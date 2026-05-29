class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        consec = 0
        consecs = [consec]
        prev = None
        print(nums)
        if len(nums) == 0:
            return 0
        for num in nums:
            if prev == None:
                prev = num
                continue
            print(prev)
            if prev + 1 == num:
                print('here')
                consec += 1
            elif prev + 1 != num and consec > 0:
                consecs.append(consec)
                consec = 0
            prev = num
        consecs.append(consec)
        print(consecs)
        return max(consecs) + 1

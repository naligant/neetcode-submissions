class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        curr = []
        largest = 0
        if len(s) == 1:
            largest = 1
        for i in range(len(s)):
            curr = []
            curr.append(s[i])
            for j in range(i+1,len(s)):
                if s[j] not in curr:
                    print(s[i], s[j])
                    curr.append(s[j])
                    if len(curr) > largest:
                        print(len(curr))
                        largest = len(curr)
                else:
                    break
        if largest == 0 and len(curr) == 1:
            return 1
        return largest
                    
            

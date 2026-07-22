class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = None
        for char in strs:
            if common == None:
                common = char
            else:
                temp = ""
                n = min(len(common), len(char))
                for i in range(n):
                    if common[i] == char[i]:
                        temp += common[i]
                    else:
                        break
                common = temp
        return common

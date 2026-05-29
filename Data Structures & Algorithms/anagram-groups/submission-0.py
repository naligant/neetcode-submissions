class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        ans = []
        for i in range(len(strs)):
            temp = list(strs[i])
            temp.sort()
            temp = "".join(temp)
            if temp not in hashmap:
                hashmap[temp] = [i]
            else:
                hashmap[temp].append(i)
        for char in hashmap:
            temp = []
            for i in hashmap[char]:
                temp.append(strs[i])
            ans.append(temp)
        return ans
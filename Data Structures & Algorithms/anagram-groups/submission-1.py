class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indexed = []

        for i in range(len(strs)):
            indexed.append([strs[i], i])
        print(indexed)
        for i in range(len(strs)):
            temp = list(indexed[i][0])
            temp.sort()
            indexed[i][0] = "".join(temp)
        unique = {}

        for i in range(len(strs)):
            if indexed[i][0] not in unique:
                unique[indexed[i][0]] = [indexed[i][1]]
            else:
                unique[indexed[i][0]].append(indexed[i][1])
        print(unique)
        ans = []
        for i in unique:
            temp = []
            for j in unique[i]:
                print(j)
                temp.append(strs[j])
            ans.append(temp)
        return ans


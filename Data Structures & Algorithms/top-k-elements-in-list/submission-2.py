class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = {}
        list_ = []
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        for i in dict_:
            list_.append([dict_[i], i])
        list_.sort(reverse=True)
        temp = []
        for i in range(k):
            temp.append(list_[i][1])
        return temp
            
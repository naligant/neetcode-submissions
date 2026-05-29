class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        ans = []
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        # swapped_dict = {value: key for key, value in hashmap.items()}
        hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        i = 0
        for num in hashmap:
            ans.append(num)
            k -= 1
            if k == 0:
                return ans

       
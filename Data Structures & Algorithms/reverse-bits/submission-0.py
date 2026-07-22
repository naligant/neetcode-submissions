class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_ = ""
        for i in range(32):
            if n & (1 << i):
                reversed_ += "1"
            else:
                reversed_ += "0"
        
        res = 0
        for i, bit in enumerate(reversed_[::-1]):
            if bit == "1":
                res |= (1 << i)
        return res

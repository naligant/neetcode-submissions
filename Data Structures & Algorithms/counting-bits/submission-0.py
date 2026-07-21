class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []
        ans = []
        for i in range(n+1):
            bit = ""
            while i > 0:
                bit += str(i%2)
                i = i // 2
            bit = list(bit)
            bit = bit[::-1]
            bit = "".join(bit)
            bits.append(bit)
        bits[0] = '0'
        
        for i in range(len(bits)):
            cnt = 0
            temp = list(bits[i])
            for i in temp:
                if i == '1':
                    cnt += 1
            ans.append(cnt)
        return ans


        
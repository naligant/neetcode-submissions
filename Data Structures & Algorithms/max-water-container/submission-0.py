class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if (min(heights[i],heights[j]) * abs(i-j)) > largest:
                    largest = min(heights[i],heights[j]) * abs(i-j)
                    
        return largest
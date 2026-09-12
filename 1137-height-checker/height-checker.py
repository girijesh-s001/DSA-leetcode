class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height = sorted(heights)
        count = 0
        for i in range(0,len(height)):
            if height[i]!=heights[i]:
                count+=1
        return count
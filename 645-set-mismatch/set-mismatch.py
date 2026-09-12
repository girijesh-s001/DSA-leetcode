class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        dup = 0
        miss = 0
        for i in range(1,len(nums)+1):
            if i not in freq:
                miss = i
            elif freq[i]>1:
                dup = i
        
        return [dup,miss]
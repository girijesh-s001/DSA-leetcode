class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if n+1 != len(nums):
            return False
        nums.sort()
        expected = list(range(1, n+1))+[n]
        return nums==expected
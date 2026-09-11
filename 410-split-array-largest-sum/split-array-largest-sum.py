class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low < high:
            mid = (low + high) // 2
            count = 1
            current = 0
            for num in nums:
                if current + num > mid:
                    count += 1
                    current = num
                else:
                    current += num
            if count <= k:
                high = mid
            else:
                low = mid + 1
        return low
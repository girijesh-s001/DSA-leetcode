class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        # Combine pairwise intersections using bitwise OR (|)
        # An element is included if it's in (1 and 2), (1 and 3), or (2 and 3)
        res = (s1 & s2) | (s1 & s3) | (s2 & s3)
        return list(res)
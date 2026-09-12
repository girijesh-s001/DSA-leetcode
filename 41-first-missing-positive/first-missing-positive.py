class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lst = sorted(list(set(i for i in nums if i>0)))
        if not lst or lst[0]!=1:
            return 1
        else:
            for i in range(1,len(lst)):
                if lst[i-1]+1 != lst[i]:
                    return lst[i-1]+1
        return lst[-1]+1
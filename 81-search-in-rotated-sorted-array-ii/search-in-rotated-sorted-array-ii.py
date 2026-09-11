class Solution:
    def search(self, num: List[int], target: int) -> bool:
        #return target in nums
        l = 0
        r = len(num)-1
        while l<=r:
            mid = (l+r)//2
            if num[mid]==target:
                return True
            if num[l]==num[mid] and num[mid]==num[r]:
                l+=1
                r-=1
            elif num[l] <= num[mid]:
                if target >= num[l] and target < num[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > num[mid] and target <= num[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

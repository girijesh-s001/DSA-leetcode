class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            num = str(i)
            n = len(num)
            if n % 2 != 0:
                continue
            left = list(num[:n//2])
            right = list(num[n//2:])
            a = sum(map(int,left))
            b = sum(map(int,right))
            if a==b:
                count+=1
        return count
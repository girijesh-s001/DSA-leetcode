class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        num = x
        tot = 0
        while num!=0:
            tot += (num%10)
            num//=10
        if x % tot == 0:
            return tot
        return -1

class Solution:
    def isFascinating(self, n: int) -> bool:
        n1 = n*2
        n2 = n*3
        st = str(n) + str(n1) + str(n2)
        lst = [int(i) for i in st]
        lst1 = [1,2,3,4,5,6,7,8,9]
        return sorted(lst) == lst1
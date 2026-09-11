class Solution:
    def processStr(self, s: str) -> str:
        lst = []
        for i in s:
            if i == "#":
                lst *= 2
            elif i == "%":
                lst = lst[::-1]
            elif i=="*":
                lst[:]=lst[:len(lst)-1]
            else:
                lst.append(i)
        st = ""
        for i in lst:
            st += i
        return st
class Solution:
    def processStr(self, s: str) -> str:
        ans = ""
        for i in s:
            if i == "#":
                ans *= 2
            elif i == "%":
                ans = ans[::-1]
            elif i=="*":
                ans = ans[:-1]
            else:
                ans+=i
        return ans
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wavi = 0 
        for i in range(num1, num2+1):
            s = str(i)
            for j in range(1, len(s)-1):
                a = int(s[j-1])
                b = int(s[j])
                c = int(s[j+1])
                if (a>b and b<c) or (a<b and b>c):
                    wavi += 1
        return wavi
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                lst.append("FizzBuzz")
                continue
            elif i%3==0 or i%5==0:
                if i%3==0:
                    lst.append("Fizz")
                else:
                    lst.append("Buzz")
                continue
            else:
                lst.append(str(i))
        return lst
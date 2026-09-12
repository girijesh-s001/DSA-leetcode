class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = 0
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i in alphabets:
            if i not in sentence:
                return False
        return True
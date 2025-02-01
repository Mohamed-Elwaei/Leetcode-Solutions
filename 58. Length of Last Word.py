class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        while index > -1 and s[index] == ' ':
            index -= 1
        count = 0
        while index > -1 and s[index] != ' ':
            index -= 1
            count += 1
        return count
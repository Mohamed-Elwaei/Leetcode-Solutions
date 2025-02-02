class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones,zeroes = 0,0
        for c in s:
            if c == '0': zeroes+=1
            else:ones+=1
        string = ''
        string += '1' * (ones - 1)
        string += '0' * zeroes
        string += '1'
        return string
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        num = left 

        while right > left:
            num &= right
            right &= (right - 1)

        return num
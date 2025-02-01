class Solution:
    def findNthDigit(self, n: int) -> int:
        #1 - 9   we have 9 - 1 + 1 = 9      numbers and 9 * 1 digits    total = 9
        #10 - 99 we have 99 - 10 + 1 = 90   numbers and 90 * 2 digits   total = 9 + 180
        #100 - 999 we have 999 - 100 + 1 = 900   numbers and 900 * 3 digits total = 9 + 180 + 2700
        digits = start = 1
        end = 9
        total = 9
        target = n - 1
        while n > total:
            target -= (end - start + 1) * digits
            digits += 1
            start *= 10
            end = (end * 10) + 9
            total += (end - start + 1) * digits
        answer = start + (target // digits)
        target %= digits
        answer = str(answer)
        return int(answer[target])

        
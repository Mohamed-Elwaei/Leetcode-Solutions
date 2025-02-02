class Solution:
    def sumGame(self, num: str) -> bool:
        """
        Alice will always add 9 to the greater half to maximize the difference
        Bob will always add to the smaller half to minimize the difference

        30?? 0021

        """

        leftCount,rightCount = 0,0
        leftMarks, rightMarks = 0,0
        N = len(num)
        for i in range(N // 2):
            if num[i] == '?':
                leftMarks += 1
            else:
                leftCount += int(num[i])
        for i in range(N // 2, N):
            if num[i] == '?':
                rightMarks += 1
            else:
                rightCount += int(num[i])
        
        turn = 1
        while leftMarks + rightMarks > 0:
            if turn == 1: #Alice turn
                if leftCount > rightCount:
                    if leftMarks > 0:
                        leftMarks -= 1
                        leftCount += 9
                    else:
                        rightMarks -= 1
                elif rightCount >= leftCount:
                    if rightMarks > 0:
                        rightMarks -= 1
                        rightCount += 9
                    else:
                        leftMarks -= 1
            elif turn == 0: #Bob's turn
                if leftCount > rightCount:
                    if rightMarks > 0:
                        rightCount += min(leftCount - rightCount, 9)
                        rightMarks -= 1
                    else:
                        leftMarks -= 1
                elif rightCount >= leftCount:
                    if leftMarks > 0:
                        leftMarks -= 1
                        leftCount += min(rightCount - leftCount, 9)
                    else:
                        rightMarks -= 1
            turn ^= 1
        return rightCount != leftCount


s = Solution()
print(s.sumGame("25??"))
"""
A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:

It does not occupy a cell containing the character '#'.
The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.


Word can be placed backwards or in reverse.

Word can be placed in one of the n rows or m columns.

To be placed in one of these rows, the row must have one and only one consecutive sequence of empty or letter-filled cells
.the length of the sequence must be the length of the word.


So iterate over each row, and column twice.
Iterate over each row left to right, and right to left.
Iterate over each column left to right, and right to left.

"""
def F(a,b):
    if len(a) != len(b):
        return False
    n = len(a)

    for i in range(n):
        if a[i] == ' ' or a[i] == b[i]:
            continue
        else:
            return False
    return True


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        for row in board:
            curr = ''

            for c in row:
                if c == '#':
                    if F(curr,word) or F(curr[::-1],word):
                        return True
                    curr = ''
                else:
                    curr += c
            if F(curr, word) or F(curr[::-1], word):
                return True
            
        for j in range(m):
            curr = ''
            for i in range(n):
                c = board[i][j]
                if c == '#':
                    if F(curr,word) or F(curr[::-1],word):
                        return True
                    curr = ''
                else:
                    curr += c
            if F(curr,word) or F(curr[::-1], word):
                return True
        return False
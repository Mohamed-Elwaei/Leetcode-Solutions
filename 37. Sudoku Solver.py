class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        boxes,rows,cols = dict(),dict(),dict()

        for r in range(9):
            rows[r] = set(board[r])
            rows[r].remove('.')

        for c in range(9):
            cols[c] = set()
            for r in range(9):
                cols[c].add(board[r][c])
            cols[c].remove('.')
        
        for r in range(9):
            for c in range(9):
                box = (r//3) * 3 + c//3
                if box not in boxes:
                    boxes[box] = set([board[r][c]])
                else:
                    boxes[box].add(board[r][c])
        for box in boxes:
            boxes[box].remove('.')
        nums = set([str(i) for i in range(1,10)])
        def dfs():
            for r in range(9):
                for c in range(9):
                    box = (r//3) * 3 + c//3
                    if board[r][c] == '.':
                        candidates = nums.difference(boxes[box].union(rows[r].union(cols[c])))
                        if not candidates:
                            return False
                        
                        for num in candidates:
                            boxes[box].add(num)
                            rows[r].add(num)
                            cols[c].add(num)
                            board[r][c] = num
                            if dfs():
                                return True
                            boxes[box].remove(num)
                            rows[r].remove(num)
                            cols[c].remove(num)
                            board[r][c] = '.'
                        return False

            return True
        dfs()
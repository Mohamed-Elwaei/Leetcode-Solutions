class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            # Base case: Check if the current cell is out of bounds or if it's already visited or marked as 'X'.
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return

            # Mark the current 'O' as visited by changing it to 'E' (for exploration).
            board[r][c] = 'E'

            # Explore all four adjacent cells.
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # Step 1: Traverse the edges and mark 'O's connected to the border as 'E'.
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Step 2: Convert the remaining 'O's (interior 'O's) to 'X' and restore the 'E's back to 'O'.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'

                
        
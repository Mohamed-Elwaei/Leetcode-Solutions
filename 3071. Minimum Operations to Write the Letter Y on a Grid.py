"""
You are given a 0-indexed n x n grid where n is odd, and grid[r][c] is 0, 1, or 2.

Each cell can only have 3 values. 

Let the F(x,y) be a function that takes in 2 parameters: x, and y which are integers that are 0,1, or 2.
F will return the number of operations to make all cells in the 'Y' equal to x, and all cells outside 'Y' equal to y.


We return the minimum of:
F(0,1)
F(0,2)
F(1,0)
F(1,2)
F(2,0)
F(2,1)


In an nxn grid, a cell is in 'Y' if it is in row i column j such that:

i == j and i <= n//2.
i + j == n - 1 and i < j
j == n//2 and i >= n//2

"""
def F(grid, x, y):
    
    n = len(grid)
    
    operations = 0
    
    
    
    for i in range(n):
        for j in range(n):
            
            if (i == j and i <= n//2) or (i + j == n-1 and i < j) or (j == n//2 and i >= n//2): # If the cell belongs to 'Y'
                if grid[i][j] != x: #If the cell belongs to 'Y' and is not equal to x.
                    operations += 1
            elif grid[i][j] != y: #If the cell does not belong to 'Y' and is not equal to y.
                operations += 1
                
    return operations




class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        
        answer = float('inf')
        for i in range(0,3):
            for j in range(0,3):
                if i != j:
                    answer = min(answer, F(grid,i,j))
        return answer
                    
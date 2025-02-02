class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        def peak(r,c, elem):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return True
            return elem > mat[r][c]
        
        for r in range(rows):
            for c in range(cols):
                if peak(r-1,c,mat[r][c]) and peak(r+1,c,mat[r][c]) and peak(r,c - 1,mat[r][c]) and peak(r, c + 1, mat[r][c]):
                    return r,c
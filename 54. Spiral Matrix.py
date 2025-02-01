class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()

        r,c = 0,0
        rows,cols = len(matrix),len(matrix[0])

        ans = []
        right = lambda x,y: (x,y+1)
        down = lambda x,y: (x+1,y)
        left = lambda x,y: (x,y-1)
        up = lambda x,y: (x-1,y)


        directions = [right,down,left,up]
        curr = 0
        while len(visited) < rows * cols:
                if (r,c) not in visited:
                    visited.add((r,c))
                    ans.append(matrix[r][c])

                nr,nc = directions[curr](r,c)

                if nr<0 or nr>=rows or nc<0 or nc>=cols or (nr,nc) in visited:
                        curr = (curr+1)%4
                else:
                        r,c = nr,nc
        return ans
 
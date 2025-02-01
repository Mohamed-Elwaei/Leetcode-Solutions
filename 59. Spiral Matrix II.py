class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []

        for i in range(n):
            matrix.append([0] * n)
        
        visited = set()
        r,c  = 0,0

        right = lambda x,y: (x,y+1)
        down = lambda x,y: (x+1,y)
        left = lambda x,y:(x,y-1)
        up = lambda x,y:(x-1,y)
        directions = [right,down,left,up]
        
        count = 1
        curr = 0
        while len(visited) < n*n:
            visited.add((r,c))
            matrix[r][c] = count

            nr,nc = directions[curr](r,c)

            for i in range(4):
                if (nr,nc) not in visited and (0<=nr<n and 0<=nc<n):
                    break
                else:
                    curr = (curr+1)%4
                    nr,nc = directions[curr](r,c)
            r,c = nr,nc
            count+=1
        return matrix

    
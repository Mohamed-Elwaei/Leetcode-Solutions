from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        times = dict()
        rows,cols = len(grid),len(grid[0])

        fresh,rotten=0,0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c]==2:
                    rotten+=1
        if fresh and not rotten:
            return -1
        if rotten and not fresh:
            return 0
        if not rotten and not fresh:
            return 0

        def bfs(r,c):
            visited={(r,c)}
            queue = deque([(r,c, 0)])

            while queue:
                r,c,time = queue.popleft()
                visited.add((r,c))
                directions = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]

                if (r,c) not in times:
                    times[(r,c)] = time
                else:
                    times[(r,c)] = min(times[(r,c)],time)

                for d in directions:
                    if  -1< d[0] < rows and -1<d[1]<cols and (d[0],d[1]) not in visited and grid[d[0]][d[1]] == 1:
                        queue.append((d[0],d[1],time+1))
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in times:
                    times[(r,c)] = float('inf')
                if grid[r][c]==2:
                    bfs(r,c)
                    flag =1
        
        smallest = float('-inf')
        print(times)

        for t in times:
            smallest= max(smallest,times[t])

        if smallest == float('-inf') or smallest == float('inf'):
            return -1
        return smallest
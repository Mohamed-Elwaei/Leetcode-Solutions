from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        visited = set()
        queue = deque([0])

        while queue:
            u = queue.popleft()
            visited.add(u)

            for v in rooms[u]:
                if v not in visited:
                    queue.append(v)
        
        return len(visited) == len(rooms)
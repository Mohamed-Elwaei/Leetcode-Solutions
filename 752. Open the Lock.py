from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = {tuple(int(i) for i in end) for end in deadends}
        queue = deque([ [(0,0,0,0),0] ])
        target = tuple(int(i) for i in target)
        while queue:
            lock, steps = queue.popleft()
            if lock in visited: continue
            visited.add(lock)
            if lock == target:
                return steps
            for i in range(4):
                next = lock[:i] + tuple([(lock[i] + 1) % 10]) + lock[i+1:]
                prev = lock[:i] + tuple([(lock[i] - 1) % 10]) + lock[i+1:]
                queue.append([next, steps + 1])
                queue.append([prev, steps + 1])
        return -1
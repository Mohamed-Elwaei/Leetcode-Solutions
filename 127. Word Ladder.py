from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        queue = deque([(beginWord, 1)])
        words = set(wordList)
        while queue:
            curr,dist = queue.popleft()
            if curr == endWord: return dist
            for i in range(len(curr)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next = curr[:i] + c + curr[i+1:]
                    if next in words:
                        words.remove(next)
                        queue.append([next,dist + 1])
        return 0
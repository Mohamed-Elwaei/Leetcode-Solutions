
from collections import deque
def findLadders( beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        if endWord not in wordList:
             return []
        
        def valid(s,t):
            if len(s)!=len(t):
                return False
            valid = 0
            for i in range(len(s)):
                if s[i]!= t[i]:
                    valid+=1
            return valid == 1

        wordList=set(wordList)
        paths = []
        queue = deque([[beginWord]])

        while queue:
            path = queue.popleft()
            curr = path[-1]

            if valid(curr,endWord):
                paths.append(path+[endWord])
                continue

            toRemove = []
            for word in wordList:
                if valid(curr,word):
                    queue.append(path + [word])
                    toRemove.append(word)
            for r in toRemove:
                wordList.remove(r)
        return paths

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(findLadders(beginWord,endWord,wordList))
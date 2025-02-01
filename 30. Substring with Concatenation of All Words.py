class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        def insert(word):
            root = trie
            for c in word:
                if c not in root:
                    root[c] = {}
                root = root[c]
        # All the strings of words are of the same length.
        #A concatenated substring in s is a substring that contains ALL the strings of any permutation of words concatenated.
        #We want to return starting indices of all the concatenated substrings.
        #A concatenated substring has to be length M * N. where 
        N = len(words)
        M = len(words[0])
        # s = "xxbarfoofoobarthefoobarman"
        trie = {}
        words = set(words)
        removed = set()
        for word in words:
            insert(word)

        output = []
        l = r = 0
        counter = {}
        curr = trie
        tmp = ''
        while r < len(s):
            if r < len(s) and s[r] in curr and r - l + 1 < M:
                curr = curr[s[r]]
                tmp += s[r]
                if tmp in words:
                    words.remove(tmp)
                    removed.add(tmp)
                    tmp = ''
                    curr = trie
                if r - l + 1 == M: 
                    output.append(l)
                r += 1
            else:
                while l < r and s[l] in curr:
                    curr = curr[s[l]]
                    tmp += s[l]
                    if tmp in removed:
                        words.add(tmp)
                        removed.remove(tmp)
                        tmp = ''
                        curr = trie
                        break
                    l += 1
        return output

            
                
s = Solution()
print(s.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
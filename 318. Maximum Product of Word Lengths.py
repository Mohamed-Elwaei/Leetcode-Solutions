class Solution:
    def maxProduct(self, words: List[str]) -> int:

        hashes = []

        for word in words:
            num=0
            for c in word:
                num |= ( 1<<(ord(c) - ord('a')))
            hashes.append(num)
        ans =0
        for i in range(len(words)):
            for  j in range(i+1,len(words)):
                if not hashes[i] & hashes[j]:
                    ans = max(ans,len(words[i]) * len(words[j]))
        return ans
        
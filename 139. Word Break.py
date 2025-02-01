def wordBreak( s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
     
        n=len(s)
        dp = [False] * (n+1)
        dp[n]=True
        for i in range(n,-1,-1):
            for word in wordDict:
                substr=s[i:]
                if word in s[i:]:
                    dp[i] = dp[i+len(word) ]
        return dp[0]


s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s,wordDict))


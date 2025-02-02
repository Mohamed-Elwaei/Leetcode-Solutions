import string
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        perms = []
        s = [c for c in s]
        curr = ''
        def dfs(i = 0):
            nonlocal curr
            if i >= len(s):
                perms.append(curr[:])
                return

            if ord('0') <= ord(s[i]) <= ord('9'):
                curr += s[i]
                dfs(i + 1)
                curr = curr[:-1]
            elif s[i] in string.ascii_letters:
                curr += s[i].lower()
                dfs(i + 1)
                curr = curr[:-1]
                curr += s[i].upper()
                dfs(i + 1)
                curr = curr[:-1]
        dfs()
        return perms

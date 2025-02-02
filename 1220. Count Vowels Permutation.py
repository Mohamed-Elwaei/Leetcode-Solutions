
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        memo = {(c,0):1 for c in 'aeiou'}

        def dfs(letter, n):
            if (letter,n) in memo:
                return memo[(letter,n)]
            
            match letter:
                case 'a':
                    memo[(letter,n)] = dfs('e', n - 1)
                case 'e':
                    memo[(letter,n)] = dfs('a', n - 1) + dfs('i', n - 1)
                case 'i':
                    memo[(letter,n)] = dfs('a', n - 1) + dfs('e', n - 1) + dfs('o', n - 1) + dfs('u', n - 1)
                case 'o':
                    memo[(letter,n)] = dfs('i', n - 1) + dfs('u', n - 1)
                case 'u':
                    memo[(letter,n)] = dfs('a', n - 1)
                case _:
                    memo[(letter,n)] = dfs('a', n - 1) + dfs('e', n - 1) + dfs('o', n - 1) + dfs('u', n - 1) + dfs('i', n - 1)
            return memo[(letter,n)] % ((10**9) + 7)
        return dfs('',n)
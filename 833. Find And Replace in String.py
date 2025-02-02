"""

"""

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ret = ''
        n = len(s)
        i = 0

        mapping = {}
        for index,substring,target in zip(indices, sources, targets):
            x = len(substring)

            if x + index <= n and s[index:index + x] == substring:
                mapping[index] = (substring, target)




        while i < n:
            if i in mapping:
                source,target = mapping[i]

                if s[i:min(n,len(source) + i)] == source:
                    ret += target
                    i = i + len(source)
                else:
                    ret += s[i]
                    i += 1
            
            else:
                ret += s[i]
                i+=1

        return ret
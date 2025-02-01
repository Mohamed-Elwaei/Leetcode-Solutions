class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        groups = []
        curr = ''
        for c in s[::-1]:
            if c != '-':
                if c in string.ascii_lowercase:
                    c = chr(ord(c) - ord('a') + ord('A'))
                curr += c
            if len(curr) == k:
                groups.append(curr)
                curr = ''
        
        if curr:
            groups.append(curr)

        ret = ''
        groups = groups[::-1]
        for i in range(len(groups)):
            groups[i] = groups[i][::-1]
        
        return '-'.join(groups)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opens=[]
        brackets={'}':'{', ']':'[',')':'('}

        for i in s:
            if i =='{' or i=='[' or i=='(':
                opens.append(i)
            elif i =='}' or i==']' or i==')':
                if not opens:
                    return False
                if opens.pop() != brackets[i]:
                    return False
        if opens:
            return False            
        return True            
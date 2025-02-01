class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs=[]
        curr=''
        for i in path[1:]:
            if i!='/':
                curr+=i
            if i=='/':
                if curr=='..':
                    if dirs:dirs.pop()
                    curr=''
                    continue
                if curr=='.':
                    curr=''
                    continue
                if curr:
                    dirs.append(curr)
                    curr=''
        if curr=='..':
                    if dirs:dirs.pop()
                    curr=''            
                    
        if curr and curr!='.':dirs.append(curr)     
        if dirs:
            ret=''
            for i in dirs:
                ret+='/'
                ret+=i  
            return ret 
        else: return '/'         
                           
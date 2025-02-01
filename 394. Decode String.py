"""
We can have a function F that decodes the string.

as F is decoding: there are some cases
    if it runs into an open bracket,
        then F calls itself recursively.
    if it runs into a closed bracket,
        then F returns the decoded string.
    if it runs into a letter:
        F adds that letter to the decoded string.
    if it runs into a digit:
        then that means we will run into a square bracket soon, and will have to call F recursively.
    
"""
import string
class Solution:
    def decodeString(self, s: str) -> str:
        
        partition = []

        curr = ''
        open_ = closed = 0

        for c in s:
            curr += c
            if c == '[':
                open_ += 1
            elif c == ']':
                closed += 1
                if open_ == closed:
                    partition.append(curr[:])
                    curr = ''
                


        def F(s, num):

            count = ''
            decoded_string = ''
            for i in range(len(s)):
                if s[i] == '[':
                    decoded_string += F(s[i+1:], int(count))
                    break
                elif s[i] == ']':
                    break
                elif s[i] in string.digits:
                    count += s[i]
                elif s[i] in string.ascii_lowercase:
                    decoded_string += s[i]
            
            return decoded_string * (num)

        
        print(partition)
        for i in range(len(partition)):
            partition[i] = F(partition[i], 1)

        print(partition)

        return ''.join(partition)
    


s = Solution()


print(s.decodeString( "3[a]2[bc]"))
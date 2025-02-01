class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed_x=''
        x_in_string_form=str(x)
        for digit in x_in_string_form[::-1]:
            reversed_x=reversed_x+digit

        if '-' in x_in_string_form:
            return False    
        return int(reversed_x) ==x 